from django.shortcuts import render
from django.shortcuts import render ,redirect
from accounts.models import Profile, Schedule ,Notification

from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def userProfile(request):
    return render(request, template_name='accounts/userProfile.html')


def createRider(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password==cpassword and uniqueUserName(username) and len(password) > 3 and len(email)>10:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            profile = Profile.objects.create(user = user,isRider = True)
            profile.save()
            
            return render (request, template_name='pages/home.html')
            
    
    return render(request, template_name='accounts/login.html') 


def uniqueUserName(uname):
    users = User.objects.all()
    usernames = [user.username for user in users]

    if uname in usernames:
        return False
    return True

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else :
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            # else:
            #     context = { 
            #         'title':'Fail!',
            #         'm1': 'wrong password or username does not exists',
            #         'url':'home',
            #     }
            #     return render(request , 'notification/message.html' , context)

        
        return render(request, template_name='accounts/login.html')
    
    


def logOutUser(request):
    auth.logout(request)
    return redirect('/')