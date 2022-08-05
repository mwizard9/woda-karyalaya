from django.http import HttpResponse
from django.shortcuts import render
from requests import request

# Create your views here.
def index(request):
    
    return render(request, 'Index.html')

def birth(request):
        if request.method == 'POST':
            fname=request.POST['fname']
            mname=request.POST['mname']
            lname=request.POST['lname']
           
    
        return render(request, 'birth.html')

def marriage(request):
    
    return render(request, 'marriage.html')
