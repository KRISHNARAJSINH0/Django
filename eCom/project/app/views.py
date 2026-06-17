from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    search = request.GET.get('search')
    if search:
        z = Product.objects.filter(name__icontains=search)
    else:
        z = Product.objects.all()
    data = {
        'products': z}
    return render(request, 'home.html', data)

def add(request):
    name = request.GET.get('name')
    imgurl = request.GET.get('imgurl')
    description = request.GET.get('description')
    price = request.GET.get('price')
    if (name) and (imgurl) and (description) and (price):
        Product.objects.create(name=name, imgurl=imgurl, description=description, price=price)
    return render(request, 'add.html')

def show(request):
    z = Product.objects.all()
    data = {
        'products': z}
    return render(request, 'show.html', data)