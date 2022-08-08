
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
            fathername=request.POST['fathername']
            mothername=request.POST['mothername']
            marriageId=request.POST['mcer']
            img=request.POST['mimg']
            provience=request.POST['pname']
            district=request.POST['dname']
            city=request.POST['vname']
            gender=request.POST['gender']

            birth = Birth(fname=fname ,mname=mname ,lname=lname, birthday=Birthday,fathername=fathername,mothername=mothername,marriageId=marriageId,img=img,provience=provience,district=district,city=city,gender=gender)
            birth.save();
            print('user created')
            return redirect(birthc)
           
        else:
            return render(request, 'birth.html')

def marriage(request):
    
    return render(request, 'marriage.html')

def birthc(request):

    data=Birth.objects.last()
    
    return render(request, 'birth_certificate.html',{'data':data})
