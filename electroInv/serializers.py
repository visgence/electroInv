from models import Manufacture, Vendor, Type, Package, Part, Log
from rest_framework import serializers
from django.contrib.auth.models import User


class ManufactureSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Manufacture
        fields = ('name', 'website', 'contact')


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ('name', 'website', 'contact')


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'reference')


class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('name', 'library')


class PartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Part
        fields = ('part_number', 'description', 'value', 'manufacture', 'part_type',
                  'package', 'location', 'vendor', 'vendor_sku', 'qty', 'price',
                  'created', 'lastupdate')


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ('timestamp', 'part', 'action', 'qty', 'note', 'vendor', 'invoice', 'price')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
