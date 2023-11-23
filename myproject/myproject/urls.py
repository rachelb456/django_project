"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from inventory_management.views import products
from inventory_management.views import supplier
from inventory_management.views import order

from inventory_management.views import category_list
urlpatterns = [
     path('category_list/', category_list, name = 'category_list'),
      path('products/', products, name = 'products'),
      path('supplier/', supplier, name = 'supplier'),
      path('order/', order, name = 'order'),
      
]
