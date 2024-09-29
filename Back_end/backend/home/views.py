from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Offences
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')


def eligibility(request):
    if request.method == 'POST':
        Icrime = request.POST.get('crime')
        print(Icrime)
        
        #if we dont have data of an offence it would lead us to 404 to avoid it im using try and except
        try:
            info = Offences.objects.get(title=Icrime)
            print(info)
            bailable = info.bailable
            if bailable:
                print( f"offences details:{bailable}")
                messages.success(request,'You are eligible for bail',{'user_info':info})
                
                return render(request,'eligibility.html')
            else:
                messages.success(request,'You are not eligible',{'user_info':info})
                return render(request,'eligibility.html')
        except:
        
            messages.warning(request,'No such offence found in Database')
            return render(request, 'eligibility.html')
    
    else:
        offences = Offences.objects.all()
        print(offences[2].title)
        return render(request,'eligibility.html',{'offences':offences})
    
def working(request):
    return render(request,'underProcess.html')
               