from django.db import models


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=300, verbose_name="Name")
    publish_date = models.DateTimeField(auto_now=True)
    adressLine1 = models.CharField(max_length=200, verbose_name="Adress Line 1")
    adressLine2 = models.CharField(blank=True, max_length=200, verbose_name="Adress Line 2")
    area_code = models.CharField(blank=True, max_length=200, verbose_name="Area Code")
    email = models.EmailField(verbose_name="E-Mail")
    phone_number = models.CharField(max_length=200, verbose_name="Phone Number")
    city = models.CharField(blank=True, max_length=200, verbose_name="City")
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Country")
    idNumber = models.CharField(blank=True, max_length=30, verbose_name="Company ID/Org.No./CVR No.")
    document = models.FileField(blank=True, upload_to='documents/', verbose_name="Upload Files that need translating")
    freetext = models.TextField(blank=True, verbose_name="What can we help you with?")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "success/"

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField() 
    company = models.ForeignKey(
            Company,
            on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
