from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.models import User, auth
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages




# Create your views here.

def index(request):
	return render(request,'index.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request, "Invalid Credentials")
			return redirect('login.html')

	else:
		return render(request,'login.html')



def destinations(request):

	dests = Destination.objects.all()

	return render(request,'destinations.html',{'dests': dests})


def logout(request):
	auth.logout(request)
	return render(request,'logout.html')

def register(request):

	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		#try:
   		#	email = request.POST['email']
		#except MultiValueDictKeyError:
   		#	email = False
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		if(password == confirm_password):
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Already Exists!')
				return redirect('register.html')

			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email ID Already Exists!')
				return redirect('register.html')

			else:
				user = User.objects.create_user(first_name = first_name, last_name=last_name, username=username, email=email, password=password)
				user.save();
				print("User Created Successfully")
				return redirect('/')

		else:
			messages.info(request,"Passwords Not Matching")
			return redirect('register.html')

	else:
		return render(request,'register.html')




