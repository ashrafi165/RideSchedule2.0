from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, template_name='pages/home.html')


def help(request):
    
    return render(request, 'pages/help.html')


def contact(request):
    
    return render(request, 'pages/contact.html')

def rateUs(request):
    
    return render(request, 'pages/rateUs.html')

def policy(request):

    return render(request , 'pages/policy.html')