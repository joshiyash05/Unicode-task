from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import feature
# Create your views here.
def index(request):
	features = feature.objects.all()
	
	context = {
	'name':'yash',
	'age':18,
		}
	return render(request,'index.html', {'context':context,'features':features} )
def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password1 = request.POST['password1']
		if password == password1:
			if User.objects.filter(email =email).exists():
				messages.info(request,'email address already exists')
				return redirect('register')
			elif User.objects.filter(username=username).exists():
				messages.info(request,'username already exists')
				return redirect('register')
			else:
				user = User.objects.create_user(username = username, email = email , password = password)
				user.save();
				return redirect('login')
		else:
			messages.info(request,'password do not match')
			return redirect('register')
	else:
		
		return render(request,'register.html')
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'credientials invalid ')
			return redirect('login')
	else:
		return render(request,'login.html')
def logout(request):
	auth.logout(request)
	return redirect('/')