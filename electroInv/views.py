
# Local Imports
from electroInv.utils import parseDigikeyCSV
from electroInv.models import Part, Vendor, Manufacture

#   System imports
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.exceptions import ValidationError
from settings import SESSION_TIMEOUT, OCTOPART_KEY
from django.shortcuts import render
import urllib
try:
    import simplejson as json
except ImportError:
    import json


def check_access(request):
    request.session.set_expiry(SESSION_TIMEOUT)

    if request.user.is_authenticated():
        if request.user.is_active:
            return request.user
        else:
            return None
    else:
        return None


def part(request):
    return chucho(request, 'Part')


def vendor(request):
    return chucho(request, 'Vendor')


def type(request):
    return chucho(request, 'Type')


def manufacture(request):
    return chucho(request, 'Manufacture')


def package(request):
    return chucho(request, 'Package')


def log(request):
    return chucho(request, 'Log')


def chucho(request, model):

    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')
    print model
    print "here"
    return render(request, 'modelManage.html', {'model': model})


def index(request):
    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')
    return render(request, 'index.html', {})


def login_page(request):
    print "\nwe got here"
    response = check_access(request)
    if response is not None:
        return HttpResponseRedirect('/')

    t = loader.get_template('login.html')
    c = RequestContext(request, {})
    # return HttpResponse(t.render(c))
    return render(request, 'login.html', {})


def login(request):
    print "\n\nwe're here"
    response = check_access(request)
    if response is not None:
        return HttpResponseRedirect('/')
    print "response is: {}".format(response)
    error = ''
    if request.method == 'POST':
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                auth_login(request, user)

                return HttpResponseRedirect('/')
            else:
                error = "Account disabled"
        else:
            error = "Invalid login"

    return render(request, 'login.html', {'error': error})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")


def updateParts(partResults):

    returnData = []
    for result in partResults:
        if result['error'] is not None:
            returnData.append({'sku': result['sku'], 'vendor': result['vendor'], 'error': result['error']})
            continue

        try:
            part = Part.objects.get(vendor_sku=result['sku'], vendor__name=result['vendor'])
        except Part.DoesNotExist:
            msg = "Part does not exist for updating"
            returnData.append({'sku': result['sku'], 'vendor': result['vendor'], 'error': msg})
            continue

        if len(result['items']) == 0:
            msg = "Could not update part. Does not exist in Octopart database."
            returnData.append({'sku': result['sku'], 'vendor': result['vendor'], 'error': msg})
            continue

        partData = result['items'][0]

        try:
            manufacture = Manufacture.objects.get(name=partData['manufacturer']['name'])
        except Manufacture.DoesNotExist:
            manufacture = Manufacture(name=partData['manufacturer']['name'])
            try:
                manufacture.full_clean()
                manufacture.save()
            except ValidationError as e:
                msg = "Problem while creating new Manufacture with the name "
                msg += "%s for part: %s" % (partData['manufacturer']['name'], str(e))
                returnData.append({'sku': result['sku'], 'vendor': result['vendor'], 'error': msg})
                continue

        part.manufacture = manufacture
        part.part_number = partData['mpn']
        try:
            part.full_clean()
            part.save()
        except ValidationError as e:
            msg = "Problem while updating: %s" % str(e)
            returnData.append({'sku': result['sku'], 'vendor': result['vendor'], 'error': msg})
            continue

        returnData.append({'sku': result['sku'], 'vendor': result['vendor'], 'error': None})

    return returnData


def octopartUpdate(request):
    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')

    if OCTOPART_KEY == '':
        return HttpResponseNotFound(json.dumps({"error": 'No octopart key available'}), content_type="application/json")

    try:
        parts = json.loads(request.POST['parts'])
    except KeyError:
        return HttpResponseNotFound(json.dumps({"error": 'Server recieved no parts'}), content_type="application/json")
    except TypeError:
        return HttpResponseBadRequest(json.dumps({"error": 'Server recieved bad json'}), content_type="application/json")

    qList = []
    qResults = []
    limit = 20
    for i, part in enumerate(parts):
        q = {}
        q['sku'] = part['sku']
        q['seller'] = part['vendor']
        q['limit'] = 1
        qList.append(q)
        limit -= 1

        if limit == 0 or i == len(parts)-1:
            url = 'http://octopart.com/api/v3/parts/match?queries=%s' % urllib.quote(json.dumps(qList))
            url += '&apikey='+OCTOPART_KEY
            url += '&pretty_print=true'
            url += '&exact_only=true'
            url += '&hide[]=offers'

            data = json.loads(urllib.urlopen(url).read())
            for i, result in enumerate(data['results']):
                result['sku'] = data['request']['queries'][i]['sku']
                result['vendor'] = data['request']['queries'][i]['seller']
                qResults.append(result)

            limit = 20
            qList = []

    returnData = updateParts(qResults)
    return HttpResponse(json.dumps(returnData), content_type="application/json")


def octopart(request):
    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')

    parts = Part.objects.filter(part_number='').exclude(vendor=None, vendor_sku='')

    return render(request, 'octopart.html', {'parts': parts})


def digikey(request):
    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')

    return render(request, 'digikey.html', {})


def importDigikey(request):
    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')

    invoice = request.POST.get('invoice', None)
    invoiceNumber = request.POST.get('invoiceNumber', '')

    if invoice is None or invoice == '':
        error = "You must provide a digikey invoice for importing"
        return HttpResponse(json.dumps({'errors': [error]}), content_type="application/json")

    errors = []
    invoiceData = parseDigikeyCSV(invoice)

    vendor = Vendor.objects.get(name="Digi-Key")
    for data in invoiceData:
        try:
            part = Part.objects.get(vendor_sku=data['vendor_sku'])
        except Part.DoesNotExist:
            part = Part()
            part.description = data['description']
        except KeyError:
            errors.append('Was not able to find part number in data.')
            continue

        for field, value in data.iteritems():
            if field in ['id', 'pk']:
                continue

            if field == "qty":
                part.qty += value
            else:
                setattr(part, field, value)

        part.vendor = vendor

        try:
            part.full_clean()
            part.save(invoiceNumber=invoiceNumber)
        except ValidationError as e:
            errors.append(str(e))

    return HttpResponse(json.dumps({'errors': errors}), content_type="application/json")
