
from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects
    # return render(request, 'products/home.html')  # this works before you add the {} to send jobs back html pages
    # that call this function
    return render(request, 'products/home.html', {'products':products})


def productdetail(request, product_id):
    detailproduct = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/productdetail.html', {'product':detailproduct})
