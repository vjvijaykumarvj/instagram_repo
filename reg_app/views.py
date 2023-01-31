from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from.forms import ReCaptchaField,MyForm


def Signup(request):
    if request.method == 'GET':
        return render(request,'reg_app/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        # validation part start here
        if username=='' or email == '' or password == '' or cpassword == '':
            messages.error(request,'Mandatory fields are missing')
            return render(request,'reg_app/register.html')
        # if password and cpassword matching checking
        if password != cpassword:
            messages.error(request, 'password and cpassword not matching')
            return render(request, 'reg_app/register.html')
        # User already existd leads to error
        elif User.objects.filter(username = username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'reg_app/register.html')
        # if email aleady exists leads to error
        elif User.objects.filter(email = email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'reg_app/register.html')
        # if there is no error go to login page
        else:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            messages.success(request,'Register Successfully Please Login')
            return redirect('/userlogin/')

def Userlogin(request):
    if request.method == 'GET':
        return render(request,'reg_app/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successfully')
            return redirect('/home/')
        else:
            messages.error(request, 'user and password in correct')
            return redirect('/userlogin/')
def UserlogOut(request):
    logout(request)
    return redirect('/userlogin/')


