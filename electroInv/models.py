from django.db import models
from chucho.models import ChuchoManager, ChuchoUserManager

class Manufacture(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100,blank=True,null=True)
    contact = models.CharField(max_length=100,blank=True,null=True)
    objects = ChuchoManager()

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100,blank=True,null=True)
    contact = models.CharField(max_length=100,blank=True,null=True)
    objects = ChuchoManager()

class Type(models.Model):
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    objects = ChuchoManager()

class Package(models.Model):
    name = models.CharField(max_length=100)
    library = models.CharField(max_length=100,blank=True,null=True)
    objects = ChuchoManager()


class Part(models.Model):
    manufactureNumber = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    value = models.CharField(max_length=100,blank=True,null=True)
    manufacture = models.ForeignKey('Manufacture')
    partType = models.ForeignKey('Type')
    package = models.ForeignKey('Package')
    location = models.CharField(max_length=100,blank=True,null=True)
    vendor = models.ForeignKey('Vendor')
    vendorNumber = models.CharField(max_length=100,blank=True,null=True)
    qty = models.IntegerField(default=0) #Set default to 0
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    objects = ChuchoManager()

class Log(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    part = models.ForeignKey('Part')
    action = models.CharField(max_length=100,blank=True,null=True)
    qty = models.IntegerField() #Negative for removing
    note = models.CharField(max_length=100,blank=True,null=True)
    vendor = models.CharField(max_length=100,blank=True,null=True)
    invoice = models.CharField(max_length=100,blank=True,null=True)
    price = models.FloatField()
    objects = ChuchoManager()

