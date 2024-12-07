"""
URL configuration for rideschedule project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views as b_view
from accounts import views as a_view
from schedules import views as s_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',b_view.home,name='home'),
    path('home',b_view.home,name='home'),
    
    path('loginUser',a_view.loginUser,name='loginUser'),
    path('logOutUser', a_view.logOutUser, name='logOutUser'),
    path('createRider', a_view.createRider , name = 'createRider'),
    path('profileUpdate', a_view.profileUpdate, name='profileUpdate'),
    path('changePassword',a_view.changePassword, name='changePassword'),
    
    
    path('weeklySchedule',s_view.weeklySchedule,name='weeklySchedule'),
    path('dailySchedule',s_view.dailySchedule, name='dailySchedule'),
    path('monthlySchedule',s_view.monthlySchedule, name='monthlySchedule'),
    
    path('userProfile',a_view.userProfile,name='userProfile'),
    
    path('schedulePost',s_view.schedulePost,name = 'schedulePost'),
    path('userPost',s_view.userPost,name = 'userPost'),
    path('takeSchedule <str:id>',s_view.takeSchedule,name='takeSchedule'),
    path('deleteSchedule <str:id>',s_view.deleteSchedule,name='deleteSchedule'),
    path('updateSchedule <str:id>',s_view.updateSchedule,name='updateSchedule'),
    
    path('policy', b_view.policy, name = 'policy'),
    path('rateUs', b_view.rateUs, name = 'rateUs'),
    path('help', b_view.help , name = 'help'),
    path('contact', b_view.contact , name = 'contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)