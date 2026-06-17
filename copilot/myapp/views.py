from django.shortcuts import render,HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("Hello World")
def home(request):
    return HttpResponse("This is home page")
def about(request):
    return HttpResponse("This is about page")
def contact(request):
    return HttpResponse("This is contact page")