from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from home.forms import SignUpForm



def index(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    
    all_users= get_user_model().objects.all()
    
    context= {'allusers': all_users}
       
   
   
    print('ok')
    print(all_users)
    
    print(context)
  
    return render (request, 'index.html', context)

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render (request, 'signin.html')
    return render (request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('/signin')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})