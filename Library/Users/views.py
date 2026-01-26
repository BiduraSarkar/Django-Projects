from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm

# Create your views here.
def register(request):
    #form = UserCreationForm(request.POST or None)
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"User {username} was successfully registered")
            return redirect('Users:login')

    return render(request,'Users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('Store:index')

