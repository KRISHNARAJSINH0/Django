from django.shortcuts import render
from .models import Movielist
# Create your views here.
def home(request):
    return render(request,'1.html')

def movie(request):
    se=request.GET.get("search")
    if se:
        z=Movielist.objects.filter(name__icontains=se)
    else:
        z = Movielist.objects.all()
        
    data = {"d":z}
    return render(request,"2.html",data)