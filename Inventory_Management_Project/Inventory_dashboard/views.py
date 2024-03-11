from django.shortcuts import render
from .models import Product
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def products(request):
    product_items=Product.objects.all()
    return render(request,'products.html',{'product_items':product_items})
    

    
