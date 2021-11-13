import collections
from django import http
from  django.http import HttpResponse
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts  import render, redirect , reverse
import requests

def show(request):
    a = 10
    b = 20
    c = a+b
    return HttpResponse("<h2>{}  + {} = {}</h2>".format(a,b,c))

def home(request):
    msg  = """<center> <h2> welcome to Django application </h2></center><hr/>
    <marquee>  this traing session is given by Gist Technosolution</marquee>
        <hr/>
    <a href="about_us">About Us </a> 
    <a href="our_staff"> Staff List</a>
    <a href="hello"> Click here (hello) </a>
     """
    return HttpResponse(msg)

def about(request):
    
    msg = """<h2>about us </h2> we are training providers.<br/>we are training providers.<br/>we are training providers.<br/>
    we are training providers.<br/>we are training providers.<br/>we are training providers.<br/>
    <a href="{}"> Back</a>
    """.format(request.headers.get('referer','#'))
    print('hello')
    return HttpResponse(msg,content_type='application/vnd.ms-excel')

def referex(request):
    return render(request,'referex.html')

def showHeaders(request):
    return render(request,'showHeaders.html',{'headers':request.headers})
    
def staff(request):
    faculties =['Mr. Ramesh','Mr. Suresh','Mr. Ganesh','Mrs. Namrata Joshi']
    msg = "<center><h2>List of Faculties</h2>"
    msg += "<table width='400' height='200' border='2' cellspacing='0'>";
    msg += "<tr><th>Sno</th><th>Name</th></tr>"
    for i in range(len(faculties)):
        msg += "<tr><td>{0}</td><td>{1}</td></tr>".format(i+1,faculties[i])
    msg += "</table>"
    return HttpResponse(msg)

def sqr(request,a):
    #b = int(a)*int(a)
    b = a * a
    msg= "<h2> sqr of {0} = {1}".format(a,b)
    return HttpResponse(msg)

def add(request,a=0,b=0):
    c  = a + b
    msg = f"<h2> {a} + {b} = {c}"
    return HttpResponse(msg)

def hi(request):
    return HttpResponse("Hi from Django")

def hello(request) :
    #return HttpResponse("hello")
    #return redirect(hi)
    return render(request,'hello.html',{'name':'vikas pathak','address':'nehru nagar'})

def register(request):
    return render(request,'register.html')

def saveData(request):
    msg = 'Data saved successfully !'
    return HttpResponse(msg)
    
def details(request):
    return render(request,'details.html')

def process_details(request):
    try:
        name = request.GET.get('name','Guest')
        age = int(request.GET.get('age',0))
        #gender = request.GET['gen']
        gender = request.GET.get('gen','Undefined')
        hobbies = request.GET.getlist('hobbies','None')

        detail = f"<h2> NAME : {name} <br/> Age : {age} <br/> Gender : {gender} "
        # <br/> Hobbies : {hobbies}"
        detail += "Hobbies : <br/><ol>"
        for x in hobbies:
            detail += f"<li>{x}"
        detail += "</ol></h2>"
    except :
        return HttpResponse('Some Error in Form ')
    return HttpResponse(detail)


def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        userid=request.POST['userid']
        password=request.POST['password']
        if userid=='gist' and password=='technosolutions':
            return render (request,'welcome.html',{'userid':userid})
        else:
            return render(request,'login.html',{'error_message': 'Invalid Userid or password'})



def validateLogin(request):
    if request.session.get('userid',None):
        return render(request,'login.html',{'message':'Already LoggedIn, Click on Profile'})

    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        name=request.POST['name']
        userid=request.POST['userid']
        password=request.POST['password']
        if userid=='gist' and password=='technosolutions':
            request.session['name'] = name
            request.session['userid'] = userid
            request.session['age']= 25
            request.session.set_expiry(0)
            #return render (request,'welcome.html',{'userid':userid})
            return redirect(profile)

        else:
            return render(request,'login.html',{'error_message': 'Invalid Userid or password'})

def profile(request):
    name=request.session.get('name',None)
    userid=request.session.get('userid',None)
    age = request.session.setdefault('age',30)
    print(age)
    if name and userid:
        return render(request,'profile.html',{'name':name,'userid':userid,'age':age})
    else:
        return HttpResponse('Sorry! session expired , Login again !!')



def login2(request):
    if request.method=='GET':
        userid=request.COOKIES.get('userid','')
        password=request.COOKIES.get('password','')
        return render(request,'login2.html',{'userid':userid,'password':password})
    elif request.method=='POST':
        userid = request.POST['userid']
        password = request.POST['password']
        remember =request.POST.get('remember',None)
        if userid=='gist' and password=='tech':
            if remember:
                response = render(request,'welcome.html',{'userid':userid})
                response.set_cookie('userid',userid,max_age=60)
                response.set_cookie('password',password,max_age=60)
                return response
            else:
                return render(request,'welcome.html',{'userid':userid})
        else:
            return render(request,'login2.html',{'error_message':'invalid userid or password'})
    

def op(request):
    if request.method=='GET':
        return render (request,'operations.html')
    elif request.method=='POST':
        data = request.POST.get('text','')
        result = data.upper()
        return render (request,'operations.html',{'data':data,'result':result})

def test(request):
    months =['jan','feb','march','april','may','jun','jul','aug','sep','oct','nov','dec']
    return render(request,'testing.html',{'months':months,'student':{'name':'mohan','rollno':200,'age':23,'marks':[55,44,53,56]}})

def show_content(request):
    color = request.COOKIES.get('color','black')
    #response = render(request,'show.html',{'color':color})
    if request.GET.get('color'):
        color = request.GET.get('color')
        #response = render(request,'show.html',{'color':color})
        response = HttpResponse('')
        response.set_cookie('color',color,max_age=60*60)
    return render(request,'show.html',{'color':color})

def test2(request):
    msg='Hello <strong>Dheeraj</strong>'
    months=['jan','feb','march','april','may','june']
    return render(request,'test2.html',{'data':msg,'months':months})

def home2(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def java(request):
    return render(request,'java.html')
    

def sessionTest(request):
    return render(request,'sessionTest.html')

def logout(request):
    '''try:
        del request.session['userid']
        del request.session['name']
    except:
        pass
    finally:
        return redirect(validateLogin)
    '''
    request.session.flush()
    return redirect(validateLogin)

def read(request):
    return render(request,'readsession.html')

def layout2(request):
    return render(request,'layout2.html')

def article(request):
    return HttpResponse('this is default article')


def article(request,year):
    return HttpResponse('this is is published in {}'.format(year))

#file based session
def setsession(request):
    import json
    request.session['institute'] = ' gist tehcnhosolutions'
    products ={1:{'name':'computer','price':20000},2:{'name':'printer','price':12000},
    3:{'name':'scanner','price':5000}}
    jsonproducts=json.dumps(products)
    request.session['products']=jsonproducts
    return HttpResponse('session created ')
def getsession(request):
    import json
    jsonproducts = request.session.get('products',{})
    products = dict(json.loads(jsonproducts))
    #return HttpResponse('Session value : {}'.format(request.session.get('institute','Empty')))
    #return HttpResponse(jsonproducts)
    msg = ""
    for key,product in products.items():
        msg += key +"<br/>"
        for k,v in product.items():
            msg += f"{k} :  {v} <br>"

    return HttpResponse(msg)

def delsession(request):
    request.session.flush()
    return HttpResponse('session destroyed')

def wishing(request):
    return HttpResponse('wishing from ADMIN')

def wishing1(request):
    return HttpResponse('WISHING FROM MANAGER')

def adminIndex(request):
    #link ="<br/> a href='myadmin/wish'/> goto wishing </a>"
    #return HttpResponse("<h2>ADMIN'S DASH BOARD </h2>" + link)
    
    return render(request,'adminHome.html')
    
def managerIndex(request):
    link = "<br/><a href='{}'/>goto wishing </a>".format(reverse('mwish'))
    return HttpResponse("<h2 style='color:blue'>MANAGER'S DASH BOARD </h2>" + link)

def jsonex(request):
    return render(request,'jsonex.html')

def jsondemo(request):
    return render(request,'jsondemo.html')
def registerCity(request):
    import json
    city =request.GET.get("city","");
    cities=["bhopal","indore","gwalior","jabalpur","ujjain","raipur","delhi"]
    msg={};
    if city in cities:
        msg={"type":"success","message":"city is available"}
        #return HttpResponse("<font color='blue'><b>City is Available</b></font>")
    else:
        #return HttpResponse("<font color='red'><b>Sorry ! This is not a valid city</b></font>")
        msg={"type":"error","message":"Sorry this city is not valid"}
    jsonData = json.dumps(msg) 
    return HttpResponse(jsonData)


def ajax1(request):
    return render(request,"ajax1.html")

    
def ajax2(request):
    return render(request,'ajaxstatecity.html')

def loadstatecity(request):
    import json
    states ={0:'mp',1:'up',2:'bihar',3:'maharastra'}
    cities = {0:['bhopal','indore','jabalpur'],
    1:['allahabad','banaras','lukhnow'],
    2:['patna','gaya','sasaram'],
    3:['mumbai','nagpur','pune']
    }
    req = request.GET.get('req','')
    if req=='states':
        st = json.dumps(states)
        return HttpResponse(st)

    elif req=='city':
        state=int(request.GET.get('state',-1))
        print(state)
        ct = cities.get(state,[])
        ct = json.dumps(ct)
        return HttpResponse(ct)

def ajax3(request):
    return render(request,'ajax3.html')

def ajax3Process(request):
    import json
    data = request.GET.get('json',[])
    print('data is ',data, '\n length is ',len(data))
    persons = json.loads(data)
    n  =len(persons)
    return HttpResponse("Total %d Records Received by the server"%n)


def getMeaing(request):
    import json
    app_id = "0fdf1b1f"
    app_key = "f7017ac274470927ca86de819ff98089"
    language = "en-gb"
    word_id = request.GET.get('word','example')
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    return HttpResponse(r)

def dictForm(request):
    return render(request,'dict.html')

def sendSms(request):
    import json
    #message = request.GET.get("message","this is hello from gist")
    data ='ABCDEFGH234IJKLM5678NOPQRS0TUVWXYZ4&*'
    otp=''
    import random
    for x in range(6):
        otp = otp+random.choice(data)
    
    message = otp
    numbers = request.GET.get("numbers")
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"RVq3p7bGsHcr1uJQ04FEY5TlaPyOUSz6n9MxjZWI8tdiDwvmeXtlpPYOHk9WLzyd2rnNIVRiUSZ0f8FC","sender_id":"TXTIND","message":f"{message}","route":"v3","numbers":f"{numbers}"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    output = {'server_output':response.text,'otp':otp}
    return HttpResponse(json.dumps(output))

def smsSender(request):
    return render(request,'smsSender.html')