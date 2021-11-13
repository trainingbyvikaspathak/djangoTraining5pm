from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminIndex,),
    path('wish/',views.wishing,name='awish') 
]