
from schedules.models import Schedule
from django.contrib.auth.models import User, auth

from django.shortcuts import render ,redirect
from accounts.models import Profile,Notification
from schedules.models import Schedule

from .scheduleForm import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def weeklySchedule(request):
    if request.method == 'POST':
        rider = request.user.profile
        pickUp_time = request.POST.get('startTime')
        pickUp_from = request.POST.get('picklocation')
        drop_to = request.POST.get('droplocation')
        price = request.POST.get('SPrice')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        week=''
        if(request.POST.get('SUN')): week = week+request.POST.get('SUN')
        if(request.POST.get('MON')): week = week+' '+request.POST.get('MON')
        if(request.POST.get('TUE')): week = week+' '+request.POST.get('TUE')
        if(request.POST.get('WED')): week = week+' '+request.POST.get('WED')
        if(request.POST.get('THE')): week = week+' '+request.POST.get('THE')
        if(request.POST.get('FRI')): week = week+' '+request.POST.get('FRI')
        if(request.POST.get('SAT')): week = week+' '+request.POST.get('SAT')

        schedule = Schedule.objects.create(rider_id=rider,pickUp_time=pickUp_time,pickup_from=pickUp_from,drop_to=drop_to,type_of_schedule='weekly',price=price,startDate=startDate,endDate=endDate,weeks=week)
        schedule.save()
        context = { 
            'title':'Successfull',
            'm1': 'schedule created successfull',
            'url':'home',
            }
        return render(request , 'notification/message.html' , context)

    return render(request,'schedule/weeklySchedule.html')

@login_required(login_url='login')
def monthlySchedule(request):
    if request.method == 'POST':
        rider = request.user.profile
        pickUp_time = request.POST.get('startTime')
        pickUp_from = request.POST.get('picklocation')
        drop_to = request.POST.get('droplocation')
        price = request.POST.get('SPrice')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        week=''
        if(request.POST.get('SUN')): week = week+request.POST.get('SUN')
        if(request.POST.get('MON')): week = week+' '+request.POST.get('MON')
        if(request.POST.get('TUE')): week = week+' '+request.POST.get('TUE')
        if(request.POST.get('WED')): week = week+' '+request.POST.get('WED')
        if(request.POST.get('THE')): week = week+' '+request.POST.get('THE')
        if(request.POST.get('FRI')): week = week+' '+request.POST.get('FRI')
        if(request.POST.get('SAT')): week = week+' '+request.POST.get('SAT')

        schedule = Schedule.objects.create(rider_id=rider,pickUp_time=pickUp_time,pickup_from=pickUp_from,drop_to=drop_to,type_of_schedule='monthly',price=price,startDate=startDate,endDate=endDate,weeks=week)
        schedule.save()
        context = { 
            'title':'Successfull',
            'm1': 'schedule created successfull',
            'url':'home',
            }
        return render(request , 'notification/message.html' , context)


    return render(request,'schedule/monthlySchedule.html')

@login_required(login_url='login')
def dailySchedule(request):
    if request.method == 'POST':
        rider = request.user.profile
        pickUp_time = request.POST.get('startTime')
        pickUp_from = request.POST.get('picklocation')
        drop_to = request.POST.get('droplocation')
        price = request.POST.get('SPrice')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')

        schedule = Schedule.objects.create(rider_id=rider,pickUp_time=pickUp_time,pickup_from=pickUp_from,drop_to=drop_to,type_of_schedule='daily',price=price,startDate=startDate,endDate=endDate)
        schedule.save()
        context = { 
            'title':'Successfull',
            'm1': 'schedule created successfull',
            'url':'home',
            }
        return render(request , 'notification/message.html' , context)


    return render(request,'schedule/dailySchedule.html')


@login_required(login_url='login')
def schedulePost(request):
    schedulePost = Schedule.objects.all().order_by("pickUp_time")

    posts = {
        'schedulePost': schedulePost,
        
    }
    return render(request, template_name='schedule/SchedulePost.html', context=posts)

@login_required(login_url='login')
def userPost(request):
    schedulePost = Schedule.objects.all().order_by("pickUp_time")

    posts = {
        'schedulePost': schedulePost,
        
    }
    return render(request, template_name='accounts/userPost.html', context=posts)


@login_required(login_url='login')
def takeSchedule(request , id):
    schedule= Schedule.objects.get(pk = id)
    
    context={
        'title':'Take Schedule',
        'm2':'Do you want to take this schedule?',
        'text1': 'From: '+schedule.pickup_from +'\n To: '+schedule.drop_to,
        'text2': 'Price: '+str(schedule.price)+'TK',
        'url':'schedulePost',
    }
    if request.method == 'POST':
        schedule.pending = False
        schedule.driver_id = request.user.username
        schedule.save()
        
        return redirect('schedulePost')
    return render(request, 'notification/confirm.html',context)