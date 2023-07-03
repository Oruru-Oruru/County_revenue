"""Huduuma_Bora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from county_revenue import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("mpesa_express/", views.mpesa_express, name="mpesa_express"),

    path('', views.index, name='home'),
    
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path('logout/', views.logout_user, name='logout'),
    path('defaulters/', views.track_defaulters, name='defaulters'),
    path('track_defaulters/', views.track_defaulters, name='defaulters'),
    path('county_customer/', views.create_county_customer, name='county_customer'),
    path('enterprise/', views.create_enterprise, name='enterprise'),
    path('enterprise_list/', views.enterprise_list, name='enterprise_list'),
    path('revenue/', views.create_revenue, name='revenue'),
    path('revenue_list/', views.revenue_list, name='revenue_list'),
    path('invoice/', views.create_invoice, name='invoice'),
    path('invoice_list/', views.invoice_list, name='revenue_list'),
    path('service/', views.create_service, name='service'),
    path('service_list/', views.service_list, name='service_list'),
    path('track_defaulters.html/', views.track_defaulters , name='track_defaulters'),
    path('pdf/', views.pdf, name="system_report"),
    
    #path('defaulters/', views.track_defaulters, name='track_defaulters'),
    
    
    
    
]
