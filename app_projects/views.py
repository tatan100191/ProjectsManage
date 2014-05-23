from django.contrib.auth.models import User
from django.shortcuts import render 
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def user(request):
	return render(request,'createUser.html')

def createUser(request):
	username = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	user = User.objects.create_user(username, email, password)	
	user.save()
	return HttpResponseRedirect(reverse('django.contrib.auth.views.logout'))

def permission(request):
	return render(request,'permission.html')