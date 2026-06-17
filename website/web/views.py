from django.shortcuts import render
from .models import Store
# Create your views here.
def home(request):
    return render(request, 'home.html')
def add(request):
    name  = request.GET.get('item')
    price = request.GET.get('price')
    if (name) and (price):
        Store.objects.create(name=name, price=price)
    return render(render,'add.html')

def show(request):
    z = Store.objects.all()
    data = {"d":z}
    return render(request, 'show.html', data)