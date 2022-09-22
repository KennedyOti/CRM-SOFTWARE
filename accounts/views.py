from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.


#THE HOME PAGE FUNCTION VIEW
def home(request):
    customers = Customers.objects.all()
    orders = Orders.objects.all()
    products = Products.objects.all()

    total_orders = orders.count()
    total_products = products.count()
    total_customers = customers.count()
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()

    context = {'orders':orders, 'customers':customers, 'total_customers':total_customers, 'total_products':total_products,
     'total_orders':total_orders, 'pending_orders':pending_orders, 'delivered_orders':delivered_orders}

    return render(request, 'accounts/dashboard.html', context)

#THE PRODUCTS PAGE FUNCTION VIEW
def products(request):
    products = Products.objects.all()
    return render(request, 'accounts/products.html', {'products' :products})

#THE PRODUCTS PAGE FUNCTION VIEW
def customers(request, pk):
    customer = Customers.objects.get(id=pk)

    orders = customer.orders_set.all()
    orders_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'orders_count':orders_count}
    return render(request, 'accounts/customers.html',context)



