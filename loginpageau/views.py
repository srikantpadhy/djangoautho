from django.http import FileResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext


# Create your views here.
def home(request):
    return render(request,'home.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        my_user =  User.objects.create_user(username,email,password1)
        my_user.save()
        print(username,email,password1,password2)
        return redirect('login')
    return render(request,'signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request, user)
            img = open(r"C:\Users\user\Pictures\Camera Roll\WIN_20250202_02_18_33_Pro.jpg", 'rb')
            response = FileResponse(img)
            return response
            # return redirect('home')

    return render(request,'login.html')
def dashboard(request):
    pass
def logout_view(request):
    logout(request)
    return redirect('register_view')


# def send_file(response):
#     img = open(r"C:\Users\user\Pictures\Camera Roll\WIN_20250202_02_18_33_Pro.jpg", 'rb')
#     response = FileResponse(img)
#     return response