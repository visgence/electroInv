from models import Type, Vendor, Manufacture
from rest_framework import serializers


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'reference', 'objects')


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ('name', 'website', 'contact', 'objects')


class ManufactureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacture
        fields = ('name', 'website', 'contact', 'objects')


