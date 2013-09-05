
#Local Imports
from electroInv.utils import parseDigikeyCSV
from electroInv.models import Part, Vendor

#System imports
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.exceptions import ValidationError
from settings import SESSION_TIMEOUT

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
	return chucho(request,'Part')
def vendor(request):
	return chucho(request,'Vendor')
def type(request):
	return chucho(request,'Type')
def manufacture(request):
	return chucho(request,'Manufacture')
def package(request):
	return chucho(request,'Package')
def log(request):
	return chucho(request,'Log')

def chucho(request,model):
   
    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')
    
    t = loader.get_template('modelManage.html')
    c = RequestContext(request, {'model':model})
    return HttpResponse(t.render(c))


def index(request):
   
    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')
    
    t = loader.get_template('index.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))


def login_page(request):

    response = check_access(request)
    if response is not None:
        return HttpResponseRedirect('/')

    t = loader.get_template('login.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))


def login(request):
    
    response = check_access(request)
    if response is not None:
        return HttpResponseRedirect('/')

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
            error = "Invalid login";

    t = loader.get_template('login.html');
    c = RequestContext(request, {'error':error})
    return HttpResponse(t.render(c))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")


def digikey(request):

    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')

    t = loader.get_template('digikey.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))


def importDigikey(request):
    
    response = check_access(request)
    if response is None:
        return HttpResponseRedirect('/electroInv/login-page/')

    invoice = request.POST.get('invoice', None)
    if invoice is None or invoice == '':
        error = "You must provide a digikey invoice for importing"
        return HttpResponse(json.dumps({'errors': [error]}), content_type="application/json")

    errors = []
    invoiceData = parseDigikeyCSV(invoice)

    vendor = Vendor.objects.get(name="Digi-Key")
    for data in invoiceData:
        try:
            part = Part.objects.get(vendor_sku = data['vendor_sku'])
        except Part.DoesNotExist:
            part = Part()
            part.description=data['description']
        except KeyError:
            errors.append('Was not able to locate vendor sku.')
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
            part.save()
        except ValidationError as e:
            errors.append(str(e))

    return HttpResponse(json.dumps("Success!"), content_type="application/json")


