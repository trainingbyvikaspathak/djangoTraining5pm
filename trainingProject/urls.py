"""trainingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views,adminurls, managerurls
import myapp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('',views.home, name='home'),
    path('',views.home2,name='home2'),
    path('admin/', admin.site.urls),
    #path('add/',views.show),
    path('about_us/',views.about, name='about_us'),
    path('our_staff/',views.staff,name='our_staff'),
    path('sqr/<int:a>',views.sqr,name='sqr'),
    path('add/',views.add,name='add1'),
    path('add/<int:a>/',views.add,name='add2'),
    path('add/<int:a>/<int:b>',views.add,name='add'),
    path('hi/',views.hi,name='hi'),
    path('hello/',views.hello,name='hello'),
    path('register/',views.register,name='register'),
    path('save/',views.saveData,name='save'),
    path('details/',views.details,name='details'),
    path('process_details/',views.process_details,name='process'),
    #path('login/',views.login,name='loging'),
    path('login/',views.validateLogin,name='login'),
    path('validate/',views.validateLogin,name='validate'),
    path('login2/',views.login2,name='login2'),
    path('operation/',views.op,name='op')  ,
    path('test/',views.test,name='test') ,
    path('show/',views.show_content,name='show'),
    path('test2/',views.test2,name='test2'),
    path('contact-us',views.contact,name='contact'),
    path('java-syllabus',views.java,name='java'),
    path('profile',views.profile,name='profile'),
    path('session/',views.sessionTest,name='session'),
    path('logout/',views.logout,name='logout'),
    path('read/',views.read,name='read'),
    path('layout2/',views.layout2,name='l2'),
    path('setsession/',views.setsession),
    path('getsession/',views.getsession),
    path('delsession/',views.delsession),
    path('myadmin/',include(adminurls)),
    path('manager/',include(managerurls)),
    path('referex/',views.referex),
    path('showheaders/',views.showHeaders),
    path('jsonex/',views.jsonex),
    path('jsondemo/',views.jsondemo),
    path('registerCity/',views.registerCity,name='registerCity'),
    path('ajax1/',views.ajax1),
    path('ajax2/',views.ajax2),
    path('loadstatecity/',views.loadstatecity,name='loadstatecity'),
    path('ajax3/',views.ajax3,name='ajax3'),
    path('ajax3Process/',views.ajax3Process,name='ajax3Process'),
    path('dictionary/',views.getMeaing,name='dictionary'),
    path('dictForm/',views.dictForm,name='dictForm'),
    path('sendSms/',views.sendSms,name='sendSms'),
    path('smsSender/',views.smsSender,name='smsSender'),
    path('myapp/',include('myapp.urls'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

