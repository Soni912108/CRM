from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect



def home(request):
    return render(request,'home/index.html')



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('crm:dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('crm:dashboard')  # Assuming you have a 'dashboard' URL in the 'crm' app
    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {'form': form})