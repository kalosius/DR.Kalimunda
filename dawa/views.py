from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Sale
#now we are including our filters from the filters file
from .filters import Product_filter

# including our model forms created in the forms file
from .forms import AddForm, SaleForm


# Create your views here.

def index(request):
    products = Product.objects.all().order_by('-id')
    product_filter = Product_filter(request.GET, queryset=products)
    products = product_filter.qs
    return render(request,'products/index.html', {'products':products,'product_filter':product_filter})

@login_required
def home(request):
    return render(request, 'products/aboutDrkali.html')



# Create a view for product_detail
# @login_required is a decorator, it comes before a function

@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'products/products_detail.html', {'product': product})

@login_required
def issue_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)

    if request.method == 'POST':
        #check if required input is as is supposed to be
        if sales_form.is_valid():
            new_sales = sales_form.save(commit = False)
            new_sales.item = issued_item
            new_sales.unit_price = issued_item.unit_price
            new_sales.save()
            #to keep track of remainding stock aftr sale
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)

            return redirect('reciept')
    return render(request, 'products/issue_item.html', {'sales_form':sales_form})

@login_required
def reciept(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'products/reciept.html', {'sales': sales})





@login_required
def add_to_stock(request, pk):
    pass


