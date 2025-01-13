from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from user_profile.models import Profile

def home(request):
    return render(request, 'core_app/home.html', {'title': 'Home'})

def login(request):
    return render(request, 'core_app/login.html', {'title':'Login'})

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email already exists')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
            else:
                new_user= User.objects.create_user(
                    first_name=first_name,
                    last_name= last_name,
                    username=username,
                    email=email,
                    password=password
                )
                new_user.save()
                get_new_user = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=get_new_user)
                new_profile.save()                
                #login the user using credentiols
                user_credential = auth.authenticate(username=username, password=password)
                auth.login(request, user_credential)
                messages.success(request,'Account is created succesfully')
                return redirect('core_app:home')
        else:
            print('password does not match')
            return redirect('core_app:signup')
    return render(request, 'core_app/signup.html', {'title':'signup'})

def logout(request):
    auth.logout(request)
    return redirect('core_app:login')
