from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'name': 'Krishnaraj',
        'surname': "solanki",
        'city': 'Rajkot'}
    return render(request, '1.html',{"d":data})

def data(request):
    data = {
        'roll_number': '28',
        'marks': [20, 30, 40, 50],
        'city': ['Rajkot', 'Ahmedabad', 'Surat', 'Vadodara'],
        'subject': 'Python'}
    return render(request, '2.html',{"d":data})
def base(request):
    return render(request, 'base.html')