from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def loginuser(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Login Success')
            return redirect('')
        else:
            messages.warning(request, 'Username or Password is wrong')
            return redirect('loginuser/')

    return render(request, 'loginuser.html', {'form':form})

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login (request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Username Or Password is incorrect!')
            return redirect('log')
        
    return render(request, 'log.html')