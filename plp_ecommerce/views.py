from django.shortcuts import render, get_list_or_404
from .models import Customer, Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'plp_ecommerce/product_list.html',context)

def product_detail(request, pk):
    Product = get_list_or_404(Product, pk=pk)
    context = {
        'product': Product
    }
    return render(request, 'plp_ecommerce/product_detail.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'plp_ecommerce/customer_list.html', context)

def customer_detail(request, pk):
    customer = get_list_or_404(Customer, pk=pk)
    context = {
        'customer': customer
    }
    return render(request,'plp_ecommerce/customer_detail.html', context)
    
