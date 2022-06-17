from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home',views.home, name='home'),
    path('menu',views.menu, name='menu'),
    path('tablebook',views.tablebook, name='tablebook'),
    path('login',views.signin, name='login'),
    path('signup',views.signup, name='signup'),
    path('selecttable',views.selecttable, name='selecttable'),
    path('userprofile',views.userprofile, name='userprofile'),
    path('adminpage',views.adminpage, name='adminpage'),
    path('about',views.about, name='about'),
    path('adminLogin',views.adminLogin , name='adminLogin'),
    path('manageUser',views.manageUser , name='manageUser'),
    path('manageFoodItem',views.manageFoodItem , name='manageFoodItem'),
    path('seeMsg',views.seeMsg , name='seeMsg'),
    path('order',views.order , name='order'),
    path('table',views.table , name='table'),
  
    

]