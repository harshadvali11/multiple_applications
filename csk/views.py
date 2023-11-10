from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def msd(request):
    return render(request,'msd.html')

def raina(request):
    return HttpResponse('<h1>Mr IPL</h1>')