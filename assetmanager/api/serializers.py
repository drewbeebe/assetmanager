# api/serializers.py
from rest_framework import serializers
from manufacturers.models import Manufacturer
from hardware.models import Hardware
from companies.models import Company
from models.models import Model
from locations.models import Location
from categories.models import Category
from status_labels.models import Status_label
from departments.models import Department
from information_systems.models import Information_System


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = (
            #'order_id',
            'uuid',
            'name',
            'url',
            'support_url',
            'support_phone',
        )

class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardware
        fields = (
            #'order_id',
            'uuid',
            'name',
            'asset_tag',
            'ip_address',
            'purchase_date',
            'purchase_cost',
            #'assigned_to',
            #'company_id',
            #'location_id',
            'notes',
            'physical',
            'categorization',
        )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            #'order_id',
            'uuid',
            'name',
            'url',
          )

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = (
            #'order_id',
            'uuid',
            'name',
            'modelno',
            'url',
            'manufacturer_id',
          )

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            #'order_id',
            'uuid',
            'name',
            'city',
            'state',
            'country',
            #'user_id',
          )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            #'order_id',
            'uuid',
            'name',
            'type',
          )

class Status_labelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status_label
        fields = (
            #'order_id',
            'uuid',
            'name',
          )

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            #'order_id',
            'uuid',
            'name',
          )

class Information_SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information_System
        fields = (
            #'order_id',
            'uuid',
            'name',
            'owner',
            'administrator',
          )