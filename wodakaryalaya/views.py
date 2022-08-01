from django.http import HttpResponse
from django.shortcuts import render
from requests import request

# Create your views here.
def index(request):
    
    return render(request, 'Index.html')

def birth(request):
    
    return render(request, 'birth.html')
