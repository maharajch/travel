from django.urls import path
from . import views


urlpatterns =[

path('',views.index,name='index'),
path('home',views.index,name='index'),
path('login.html',views.login,name="login"),
path('destinations.html',views.destinations,name="destinations"),
path('register.html',views.register,name="register"),
path('logout.html',views.logout,name="logout"),
]