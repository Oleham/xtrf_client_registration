from django.urls import path
from . import views

urlpatterns = [
        path('success/', views.successView, name='success'),
        path('', views.CompanyCreate.as_view(), name='index')
        ]
