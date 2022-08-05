from django.http import HttpResponse
from django.shortcuts import render
from requests import request
from .models import Birth

# Create your views here.
def index(request):
    
    return render(request, 'Index.html')

def birth(request):
        if request.method == 'POST':
            fname=request.POST['fname']
            mname=request.POST['mname']
            lname=request.POST['lname']
            Birthday=request.POST['birthday']

            birth = Birth.objects.create_user(firstname=fname,mname=mname ,lastname=lname)
            birth.save();
            print('user created')
           
        else:
            return render(request, 'birth.html')

def marriage(request):
    
    return render(request, 'marriage.html')
