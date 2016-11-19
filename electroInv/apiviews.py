from models import Vendor, Type, Manufacture, Package, Part, Log
from rest_framework import viewsets
from serializers import VendorSerializer, TypeSerializer, ManufactureSerializer, PackageSerializer, PartSerializer, LogSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics
# from rest_framework import filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
import rest_framework_filters as filters


class ManufactureViewSet(viewsets.ModelViewSet):
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_backends = (filters.SearchFilter,)
    filter_fields = ('name', 'website')
    search_fields = ('name', 'website')


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('name', 'website', 'contact')
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('__all__')


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('name', 'reference')


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('name', 'library')


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('part_number', 'value', 'manufacture', 'part_type', 'package', 'location', 'vendor', 'qty', 'price', 'created', 'lastupdate')


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('timestamp', 'part', 'action', 'qty', 'vendor', 'invoice', 'price')


class Main(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('part_number', 'value')
