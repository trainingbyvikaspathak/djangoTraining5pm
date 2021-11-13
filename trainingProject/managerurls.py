from django.urls import path
from . import views

urlpatterns = [
    path('',views.managerIndex),
    path('wish/',views.wishing1,name='mwish') 
]