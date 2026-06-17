from django.contrib import admin
from django.urls import path
from t3 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('show/',views.show,name='show'),
]
