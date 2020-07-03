from django.shortcuts import render, redirect 
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserForm, LoginForm, UpdateForm


@login_required(login_url='accounts:login')
def account(request):
	return render(request, 'account/account.html',{})


def login_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_superuser:
					login(request, user)
					next_url = request.GET.get('next')
					if next_url:
						return redirect(next_url)
					return redirect('accounts:index')

			else:
				messages.error(request,'Your account not admin')
	else:
		form = LoginForm()
	context = {'form':form}
	return render(request, 'account/login.html', context)


@login_required(login_url='accounts:login')
def logout_page(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')
	return render(request, 'account/logout.html',{})



@login_required(login_url='accounts:login')
def list_user(request):
	list_user = User.objects.all().exclude(username='admin')
	context = {'list_user':list_user}

	return render(request, 'account/list_user.html', context)
	

@login_required(login_url='accounts:login')
def create_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account was created')
			return redirect('accounts:list_user')
		else:
			messages.error(request, 'Account not created')
	else:
		form = UserForm()
	return render(request, 'account/create_user.html', {'form':form})


@login_required(login_url='accounts:login')
def delete_user(request, pk):
	user = User.objects.get(pk=pk)
	if request.method == 'POST':
		user.delete()
		return redirect('accounts:list_user')
	return render(request, 'account/delete_user.html', {'user':user})


@login_required(login_url='accounts:login')
def update_user(request, pk):
	user = User.objects.get(pk=pk)
	form = UpdateForm(instance=user)
	if request.method == 'POST':
		form = UpdateForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('accounts:list_user')

	context = {'form':form}
	return render(request, 'account/update_user.html', context)

