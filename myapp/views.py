from django.shortcuts import render

# Create your views here.
def home(request):
    #return render(request,'myapp/home.html',{'name': 'amit kumar'})
    return render(request,'myapp/index.html')

def about(request):
    return render(request,'myapp/about.html',{'center':'Gist technosolutions'})

def contact(request):
    return render(request,'myapp/contact.html')