# api/views.py
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet

from django.db.models.fields import CharField
from django.db.models import Q, Count
from . import cipher

# local imports
from manufacturers.models import Manufacturer
from hardware.models import Hardware
from companies.models import Company
from models.models import Model
from locations.models import Location
from categories.models import Category
from status_labels.models import Status_label
from departments.models import Department
from information_systems.models import Information_System
from . import serializers
from .serializers import ManufacturerSerializer, HardwareSerializer, CompanySerializer, ModelSerializer, LocationSerializer, CategorySerializer, Status_labelSerializer, DepartmentSerializer, Information_SystemSerializer

# EncryptedField
class EnField(CharField):
    #def from_db_value(self, value, expression, connection):
    def from_db_value(self, value):
        """ Decrypt the data for display in Django as normal. """
        return cipher.decrypt(value)
    def get_prep_value(self, value):
        """ Encrypt the data when saving it into the database. """
        return cipher.encrypt(value)
    #Usage: EnField(max_length=12, choices=RISK_RATING_CHOICES, default='MODERATE')


### Manufacturers
class ManufacturerViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Manufacturer
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,  # handles GETs for many Manufacturers
                     DestroyModelMixin):  # handles DELETEs for 1 Manufacturer
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

### Hardware
class HardwareViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Hardware
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,  # handles GETs for many Hardwares
                     DestroyModelMixin):  # handles DELETEs for 1 Hardware
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = HardwareSerializer
    queryset = Hardware.objects.all()

### Companies
class CompanyViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,  # handles GETs for many Companies
                     DestroyModelMixin):  # handles DELETEs for 1 Company
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

### Models
class ModelViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Model
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,  # handles GETs for many Models
                     DestroyModelMixin):  # handles DELETEs for 1 Model
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = ModelSerializer
    queryset = Model.objects.all()

### Locations
class LocationViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Location
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,  # handles GETs for many Locations
                     DestroyModelMixin):  # handles DELETEs for 1 Location
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

### Categories
class CategoryViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Category
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,  # handles GETs for many Categories
                     DestroyModelMixin):  # handles DELETEs for 1 Category
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

### Status_labels
class Status_labelViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Status_label
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,  # handles GETs for many Status_label
                     DestroyModelMixin):  # handles DELETEs for 1 Status_label
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = Status_labelSerializer
    queryset = Status_label.objects.all()


### Departments
class DepartmentViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Department
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,  # handles GETs for many Categories
                     DestroyModelMixin):  # handles DELETEs for 1 Category
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


### Information_Systems
class Information_SystemViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Department
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,  # handles GETs for many Categories
                     DestroyModelMixin):  # handles DELETEs for 1 Category
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = Information_SystemSerializer
    queryset = Information_System.objects.all()