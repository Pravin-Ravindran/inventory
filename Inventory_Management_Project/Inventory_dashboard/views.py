from django.shortcuts import render,redirect
from .models import Product
from .models import Order
from .forms import OrderForm
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def products(request):
    product_items=Product.objects.all()
    return render(request,'products.html',{'product_items':product_items})
    
def staff(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff')
    else:
        form = OrderForm()
    orders=Order.objects.all()
    return render(request,'staff.html',{'form': form, 'orders': orders})
    


    
