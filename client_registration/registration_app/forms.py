from django.forms import ModelForm
from .models import Company, Contact

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'idNumber', 'email', 'phone_number', 'adressLine1', 'adressLine2', 'area_code', 'city', 'country_id', 'document', 'freetext']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number']
