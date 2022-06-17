
from django.http import HttpResponse
from multiprocessing import context
from django.shortcuts import redirect,render
from myapp.models import Signup
from myapp.models import Message
from myapp.models import FoodItem
from myapp.models import Order
from myapp.models import TableBooking
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')
def signup(request):
  if request.method == "POST":
      username= request.POST.get('name')
      email=request.POST.get('email')
      phone=request.POST.get('phone')
      password=request.POST.get('password')

      myuser = User.objects.create_user(username, email,password)
      myuser.save()
      return redirect('login')

      
  return render( request, 'myapp/signup.html') 

  

def signin(request):

    if request.method == "POST":
        username = request.POST.get('uname')
        pass1 = request.POST['password']
        
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            return render(request, 'myapp/home.html')

        else:
            messages.error(request,"Wrong Username or Password!")
            return redirect('login')


    return render(request, 'myapp/login.html')
    
   

def home(request):
    return render(request, 'myapp/home.html')

def menu(request):
    return render(request, 'myapp/menu.html')
def tablebook(request):
    return render(request, 'myapp/tablebook.html')
     
def selecttable(request):
    return render( request, 'myapp/selecttable.html')  
def userprofile(request):
    return render( request, 'myapp/userprofile.html') 
def adminpage(request):
    return render( request, 'myapp/adminpage.html')
def about(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('msg')

        m = Message(
           name = name,
           email = email,
           message = message,
        )
        m.save()
        return redirect('about')
    return render( request, 'myapp/about.html')
def adminLogin(request):
    if request.method == "POST":
        adminName = request.POST.get('name')
        adminPassword = request.POST['password']

        if adminName=="admin" and adminPassword=="1234":
            return render(request, 'myapp/adminPage.html')
        else:
            return redirect('adminLogin')


    return render( request, 'myapp/adminLogin.html')  

def manageUser(request):
    u = User.objects.all()
    context = {
        'u' : u,
    }
    return render( request, 'myapp/manageUser.html',context)


def manageFoodItem(request):
    item = FoodItem.objects.all()
    context = {
        'item' : item,
    }
    if request.method == "POST":
        food_type = request.POST.get('type')
        food_name = request.POST.get('name')
        food_price = request.POST.get('price')

        nf = FoodItem(
           food_type = food_type,
           food_name = food_name,
           food_price = food_price,
        )
        nf.save()
        return redirect('manageFoodItem')

    return render( request, 'myapp/manageFoodItem.html',context)
def seeMsg(request):
    msg = Message.objects.all()
    context = {
        'msg' : msg,
    }
    return render( request, 'myapp/seeMsg.html',context)
def order(request):
    od = Order.objects.all()
    context = {
        'od' : od,
    }
    return render( request, 'myapp/order.html',context)
def table(request):
    t = TableBooking.objects.all()
    context = {
        't' : t,
    }
    return render( request, 'myapp/table.html',context)

    

    
    

      
  