from django.db import models
from django.contrib.auth import get_user_model
from chucho.models import ChuchoManager, ChuchoUserManager

class Manufacture(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100,blank=True)
    contact = models.CharField(max_length=100,blank=True)
    objects = ChuchoManager()
    def can_view(self, user):
        if not isinstance(user, get_user_model()):
            raise TypeError('%s is not an auth user' % str(user))

        return True
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100,blank=True)
    contact = models.CharField(max_length=100,blank=True)
    objects = ChuchoManager()
    def can_view(self, user):
        if not isinstance(user, get_user_model()):
            raise TypeError('%s is not an auth user' % str(user))

        return True

    def __unicode__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    objects = ChuchoManager()
    def can_view(self, user):
        if not isinstance(user, get_user_model()):
            raise TypeError('%s is not an auth user' % str(user))

        return True
    def __unicode__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=100)
    library = models.CharField(max_length=100,blank=True)
    objects = ChuchoManager()
    def can_view(self, user):
        if not isinstance(user, get_user_model()):
            raise TypeError('%s is not an auth user' % str(user))

        return True
    def __unicode__(self):
        return self.name


class Part(models.Model):
    part_number = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=100,blank=True)
    value = models.CharField(max_length=100,blank=True)
    manufacture = models.ForeignKey('Manufacture',blank=True,null=True)
    part_type = models.ForeignKey('Type',blank=True,null=True)
    package = models.ForeignKey('Package',blank=True,null=True)
    location = models.CharField(max_length=100,blank=True)
    vendor = models.ForeignKey('Vendor',blank=True,null=True)
    vendor_sku = models.CharField(max_length=100,blank=True)
    qty = models.IntegerField(default=0) #Set default to 0
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    lastupdate = models.DateTimeField(auto_now=True)
    objects = ChuchoManager()

    search_fields = ["part_number", "description", "manufacture", "vendor", "vendor_sku"]

    def can_view(self, user):
        if not isinstance(user, get_user_model()):
            raise TypeError('%s is not an auth user' % str(user))

        return True

    def __unicode__(self):
        if self.part_number is None:
            return ""
        return self.part_number

    def save(self, *args, **kwargs):
        
        log = True
        invoiceNumber = kwargs.pop('invoiceNumber', '')
        if 'no_log' in kwargs and kwargs['no_log'] == True:
            log = False

        action = "Added New Part"
        qty = 0

        if self.qty is not None:
            qty = int(self.qty)

        if self.id is not None:
            action = "Modified Part"
            if qty !=0:
                #Get the qty before the modifiy and save the difference
                p = Part.objects.get(id=self.id)
                qty = qty - p.qty 

        super(Part, self).save(*args, **kwargs)
       
        if log:
            l = Log(part=self,action=action,qty=qty,invoice=invoiceNumber)
            l.save()


class Log(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    part = models.ForeignKey('Part')
    action = models.CharField(max_length=100,blank=True)
    qty = models.IntegerField(blank=True,null=True) #Negative for removing
    note = models.CharField(max_length=100,blank=True)
    vendor = models.CharField(max_length=100,blank=True)
    invoice = models.CharField(max_length=100,blank=True)
    price = models.FloatField(blank=True,null=True)
    objects = ChuchoManager()
    def can_view(self, user):
        if not isinstance(user, get_user_model()):
            raise TypeError('%s is not an auth user' % str(user))

        return True



