from django.contrib.auth.signals import user_logged_in,user_login_failed,user_logged_out
from django.contrib.auth.models import User

def login_success(sender,request,user,**kwargs):
    print("LOGIN SUCCESS ")

def login_fail(sender,credentials,request, **kwargs):
    print('Ohhhhhhhh User is not valid .....')

user_logged_in.connect(login_success,sender=User)
user_login_failed.connect(login_fail)