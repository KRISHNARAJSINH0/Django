from django.shortcuts import render
from .models import Store
# Create your views here.
def home(request):
    z = Store.objects.all()
    data = {"d":z}
    return render(request,'home.html',data)
def add(request):
    if request.method == 'POST':
        name = request.POST.get('pname')
        price = request.POST.get('price')
        url = request.POST.get('img')
        desc = request.POST.get('desc')
        if (name) and (price) and (url) and (desc):
            Store.objects.create(name=name, price=price, url=url, desc=desc)
    return render(request,'add.html')
def show(request):
    return render(request,'show.html')