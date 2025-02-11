from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Product

@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})