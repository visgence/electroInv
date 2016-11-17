from models import Vendor, Type, Manufacture
from rest_framework import viewsets
from serializers import VendorSerializer, TypeSerializer, ManufactureSerializer


class VendorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ManufactureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer
