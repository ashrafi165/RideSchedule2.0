from django.shortcuts import render
from django.shortcuts import render ,redirect
from accounts.models import Profile,Notification
from schedules.models import Schedule

from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='login')
def userProfile(request):
    return render(request, template_name='accounts/userProfile.html')


def createRider(request):
    if request.method == 'POST':
        is_rider = request.POST.get('isRider')
        username = request.POST.get('usernameSignUp')
        email = request.POST.get('emailSignUp')
        password = request.POST.get('passwordSignUp')
        cpassword = request.POST.get('cpasswordSignUp')
        print("this is Rider")
        print(is_rider)
        if (password==cpassword and uniqueUserName(username) and len(password) > 3 and len(email)>10):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            is_rider_bool = is_rider == "True"
            
            profile = Profile.objects.create(user=user, isRider=is_rider_bool)
            profile.save()
            context = { 
                    'title':'Welcome',
                    'm1': username,
                    'm2':'your Driver account created successfully',
                    'm3':'Make sure to remember your username or password to Login',
                    'url':'home',
                }
            return render(request , 'notification/message.html' , context)
            
        else:
            
            context = { 
                    'title':'Fail!',
                    'm1' : 'Account already exists with this Username! or Confirm Password is wrong',
                    'm2': 'Try again',
                    'url':'home',
                }
            return render(request , 'notification/message.html' , context)
            
    
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
            else:
                context = { 
                    'title':'Fail!',
                    'm1': 'wrong password or username does not exists',
                    'url':'home',
                }
                return render(request , 'notification/message.html' , context)

        
        return render(request, template_name='accounts/login.html')
    
    

@login_required(login_url='login')
def logOutUser(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def profileUpdate(request):
    formU = UserForm()
    formP = ProfileForm()
    user = User.objects.get(username = request.user.username)
    print(user)

    pro = Profile.objects.get( user = user)
    print(pro)
    formU = UserForm(instance = user)
    formP = ProfileForm(instance = pro)
    if request.method == 'POST':
        formU = UserForm(request.POST, request.FILES, instance=user)
        formP = ProfileForm(request.POST, request.FILES, instance=pro)
        if formP.is_valid():
            formP.save()
        if formU.is_valid():
            formU.save()
        context = { 
            'title':'Successfull',
            'm1': request.user.username,
            'm2':'your profile Update Successfull',
            'url':'userProfile',
            }
        return render(request , 'notification/message.html' , context)

    context = {
        'formP':formP,
        'formU':formU
    }

    return render(request, 'update/profileUpdate.html',context)