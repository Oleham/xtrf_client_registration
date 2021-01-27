from .models import Company, Country
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'country_id']

class CompanySerializer(serializers.ModelSerializer):
    country_id = CountrySerializer
    class Meta:
        model = Company
        fields = ['id', 'name', 'idNumber', 'email', 'phone_number', 'adressLine1', 'adressLine2', 'area_code', 'city', 'country_id']
       
