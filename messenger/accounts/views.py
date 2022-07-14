from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@unauthenticated_user
def register_view(request):
    form=NewUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        user_name=form.cleaned_data.get('username')
        messages.success(request, user_name+" Successfully Registered!")
        form=NewUserForm()
        return redirect('/login/')
    context={
        'form': form,
    }
    return render(request, 'accounts/register.html', context=context)

@csrf_exempt
@unauthenticated_user
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/mails/')
        else:
            messages.info(request, "Incorrect Username/PW")
    return render(request, 'accounts/login.html', context={})

def logout_user(request):
    logout(request)
    return redirect('/login/')