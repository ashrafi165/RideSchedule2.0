from django.shortcuts import render

# Create your views here.


# Create your views here.
def weeklySchedule(request):
    return render(request, template_name='schedule/weeklySchedule.html')