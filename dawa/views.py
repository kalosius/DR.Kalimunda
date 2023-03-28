from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
#now we are including our filters from the filters file
from .filters import Product_filters


# Create your views here.

def index(request):
    products = Product.objects.all().order_by('-id')
    product_filter = Product_filters(request.GET,queryset= products)
    products = product_filter.qs
    return render(request,'index.html', {'products':products,'product_filter':product_filter})

@login_required
def home(request):
    return render(request, 'aboutDrkali.html')



# Create a view for product_detail
# @login_required is a decorator, it comes before a function

@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'products/products_detail.html', {'product': product})
