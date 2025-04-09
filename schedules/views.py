
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

from schedules.decorators import rider_required , driver_required

# Create your views here.

@rider_required(redirect_url='home')
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

@rider_required(redirect_url='home')
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

@rider_required(redirect_url='home')
def dailySchedule(request):
    if request.method == 'POST':
        rider = request.user.profile
        pickUp_time = request.POST.get('startTime')
        pickUp_from = request.POST.get('picklocation')
        drop_to = request.POST.get('droplocation')
        price = request.POST.get('SPrice')
        startDate = request.POST.get('startDate')
        # endDate = request.POST.get('endDate')

        schedule = Schedule.objects.create(rider_id=rider,pickUp_time=pickUp_time,pickup_from=pickUp_from,drop_to=drop_to,type_of_schedule='daily',price=price,startDate=startDate)
        schedule.save()
        context = { 
            'title':'Successfull',
            'm1': 'schedule created successfull',
            'url':'home',
            }
        return render(request , 'notification/message.html' , context)


    return render(request,'schedule/dailySchedule.html')


@driver_required(redirect_url='home')
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


@driver_required(redirect_url='home')
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


@login_required(login_url='login')
def deleteSchedule(request , id):
    schedule = Schedule.objects.get(pk = id)
    context={
        'title':'Delete Schedule',
        'm1':'are your sure?',
        'url':'allPostSchedule',
    }
    if request.method == 'POST':
        schedule.delete()
        return redirect('userPost')
    return render(request, 'notification/confirm.html',context)


@login_required(login_url='login')
def updateSchedule(request, id):
    try:
        schedule = Schedule.objects.get(pk = id)
        form = ScheduleForm(instance=schedule)
    
        if request.method == 'POST':
            form = ScheduleForm(request.POST, request.FILES, instance=schedule)
            if form.is_valid():
                form.save()
                context = { 
                'title':'Successfull',
                'm1': request.user.username,
                'm2':'your schedule Update Successfull',
                'url':'userPost',
                }
                return render(request , 'notification/message.html' , context)
        return render(request, 'update/updateSchedule.html',{'form': form })
    except:
        return render(request, 'update/updateSchedule.html')
    
    
def allService(request):
    return render (request, template_name='schedule/allservice.html')


@rider_required(redirect_url='home')
def parcelDelivery(request):
    if request.method == 'POST':
        rider = request.user.profile
        pickUp_time = request.POST.get('startTime')
        pickUp_from = request.POST.get('picklocation')
        drop_to = request.POST.get('droplocation')
        price = request.POST.get('SPrice')
        startDate = request.POST.get('startDate')
        weight = request.POST.get('Sweight')

        schedule = Schedule.objects.create(rider_id=rider,pickUp_time=pickUp_time,pickup_from=pickUp_from,drop_to=drop_to,type_of_schedule='Parcel Delivery',price=price,startDate=startDate,weight=weight)
        schedule.save()
        context = { 
            'title':'Successfull',
            'm1': 'Parcel Delivery schedule created successfull',
            'url':'home',
            }
        return render(request , 'notification/message.html' , context)


    return render(request,'delivery/parcel.html')

@rider_required(redirect_url='home')
def courier(request):
    if request.method == 'POST':
        rider = request.user.profile
        pickUp_time = request.POST.get('startTime')
        pickUp_from = request.POST.get('picklocation')
        drop_to = request.POST.get('droplocation')
        price = request.POST.get('SPrice')
        startDate = request.POST.get('startDate')
        weight = request.POST.get('Sweight')
        phone = request.POST.get('Sphone')
 
        schedule = Schedule.objects.create(rider_id=rider,pickUp_time=pickUp_time,pickup_from=pickUp_from,drop_to=drop_to,type_of_schedule='Courier',price=price,startDate=startDate,weight=weight,phone=phone)
        schedule.save()
        context = { 
            'title':'Successfull',
            'm1': 'Courier schedule created successfull',
            'url':'home',
            }
        return render(request , 'notification/message.html' , context)


    return render(request,'delivery/courier.html')


@rider_required(redirect_url='home')
def pharmacy(request):
    if request.method == 'POST':
        rider = request.user.profile
        pickUp_time = request.POST.get('startTime')
        pickUp_from = request.POST.get('picklocation')
        drop_to = request.POST.get('droplocation')
        price = request.POST.get('SPrice')
        startDate = request.POST.get('startDate')
        weight = request.POST.get('Sweight')
        phone = request.POST.get('Sphone')
 
        schedule = Schedule.objects.create(rider_id=rider,pickUp_time=pickUp_time,pickup_from=pickUp_from,drop_to=drop_to,type_of_schedule='Pharmacy',price=price,startDate=startDate,weight=weight,phone=phone)
        schedule.save()
        context = { 
            'title':'Successfull',
            'm1': 'Pharmacy schedule created successfull',
            'url':'home',
            }
        return render(request , 'notification/message.html' , context)


    return render(request,'delivery/pharmacy.html')
