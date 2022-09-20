from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


#THE HOME PAGE FUNCTION VIEW
def home(request):
    return render(request, 'accounts/dashboard.html')

#THE PRODUCTS PAGE FUNCTION VIEW
def products(request):
    return render(request, 'accounts/products.html')

#THE PRODUCTS PAGE FUNCTION VIEW
def customers(request):
    return render(request, 'accounts/customers.html')




