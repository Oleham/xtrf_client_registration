from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Company, Contact
from .forms import CompanyForm
from rest_framework import viewsets, permissions
from .serializers import CompanySerializer
from django.http import HttpResponse
from django.core.mail import EmailMessage
import requests as requestsLib

def successView(request):
    return HttpResponse("<h1>Thanks for getting in touch. We will get back to you ASAP</h1>")


class CompanyCreate(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = 'success/'
    template_name = "registration_app/index.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            #EMAIL
#            client_name = Company.objects.all().last().name
#            client_id = Company.objects.all().last().id
#            client_email = Company.objects.all().last().email
#            client_phone = Company.objects.all().last().phone_number
#            freetext = Company.objects.all().last().freetext
#            if not freetext:
#                client_message = "<NO TEXT>"
#            else:
#                client_message = freetext
#
#            epost = EmailMessage(
#                    "New request from The Web Site",
#                    f"New request from customer {client_name}.\nE-mail: {client_email}\nPhone No: {client_phone}\n\nThe customer wrote the following message:\n{client_message}\n\n\nTo add the customer to XTRF, use following command:\n\n>>> python myscript.py {client_id}",
#                    'test@example.com',
#                    ['test@example.com'])
#            
#            #Check for attachment
#            attachment = Company.objects.all().last().document
#            if attachment.name:
#                filename = attachment.name.lstrip("documents/")
#                filestream = attachment.read()
#                epost.attach(filename, filestream)
#            else:
#                pass
#            epost.send()
#            
#	    # You can request a web hook for Teams. By sending a request at it, you will get a simple message in Teams.
#            teamswebhook = "" #<--- Input here!
#
#            teamspayload = {"title": f"Forespørsel: {client_name} (ID: {client_id})",
#	                    "description": "Ny kunde har tatt kontakt via kontaktskjemaet på hjemmesiden",
#	                    "viewUrl": "https://adaptivecards.io",
#                            "text": f"Tekst: {client_message}. Email: {client_email}"}
#
#            responseWebHook = requestsLib.post(teamswebhook, headers={"Content-Type": "application/json"}, json=teamspayload)
#            responseWebHook.raise_for_status()
#           
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


class ContactCreate(CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'email', 'phone_number']

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API to get company information
    """
    queryset = Company.objects.all().order_by('-publish_date')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated] 
