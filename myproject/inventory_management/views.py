from django.shortcuts import render
from inventory_management.models import Category
from inventory_management.models import Order
from inventory_management.models import Supplier
from inventory_management.models import Product
from rest_framework.response import Response
from django.http import HttpResponse
import json

from datetime import datetime
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#פונקציה שמחשבת כמות במלאי
def calculate_stock_quantity(id_product,quantity_order):
    products = Product.objects.get(id_product=id_product)
    amount = products.stock_product
    products.stock_product = amount - quantity_order
    price_product=products.price_product
    products.price_product = price_product
    description_product=products.description_product
    products.description_product = description_product
    name_product=products.name_product
    products.name_product = name_product
    id_category=products.id_category
    products.id_category=id_category

    products.save()
@csrf_exempt
#קטגוריה
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = {'categories': list(categories.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        name_category=json_data['name_category']
        category = Category.objects.create(name_category=name_category)
        category.save()
        return JsonResponse({'message': 123})
@csrf_exempt
#מוצר
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = {'products': list(products.values())}
        return JsonResponse(data)
    # Convert the QuerySet to a list of dictionaries
    elif request.method == 'POST':
        
        json_data = json.loads(request.body)
        id_category=json_data['id_category']
        category = Category.objects.get(id_category=id_category)
        
        name_product=json_data['name_product']
        description_product=json_data['description_product']
        price_product=json_data['price_product']
        stock_product=json_data['stock_product']
        
        product=Product.objects.create(id_category=category,name_product=name_product,description_product=description_product,price_product=price_product,stock_product=stock_product)
        product.save()
    return JsonResponse({'message': 123})
#ספק
@csrf_exempt
def supplier(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        data = {'suppliers': list(suppliers.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        
        json_data = json.loads(request.body)
        id_supplier=json_data['id_supplier']
       
    
        name_supplier=json_data['name_supplier']
        address_supplier=json_data['address_supplier']
        phone_number_supplier=json_data['phone_number_supplier']
        supplier=Supplier.objects.create(id_supplier=id_supplier,name_supplier=name_supplier,address_supplier=address_supplier,phone_number_supplier=phone_number_supplier)
        supplier.save()
    return JsonResponse({'message': 123})
#הזמנה
@csrf_exempt
def order(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        data = {'orders': list(orders.values())}
        return JsonResponse(data)
    
    elif request.method == 'POST':
        json_data = json.loads(request.body)

        id_order=json_data['id_order']
        id_product= json_data['id_product']
        id_supplier= json_data['id_supplier']
        product = Product.objects.get(id_product=id_product)
        supplier = Supplier.objects.get(id_supplier=id_supplier)
        date_order= json_data['date_order']
        quantity_order=json_data['quantity_order']
        
        order = Order.objects.create(id_order=id_order, id_product=product, id_supplier=supplier, quantity_order=quantity_order, date_order=date_order)
        order.save()
        #עדכון כמות מוצר
        calculate_stock_quantity(id_product,quantity_order)
    return JsonResponse({'message': 123})

