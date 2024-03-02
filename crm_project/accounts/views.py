from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect



def profile_view(request):
    return render(request, 'accounts/profile.html')

def logout_view(request):
    logout(request)
    return redirect('home:home')