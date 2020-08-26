from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def welcome(request):
    nm=request.POST['name']
    return render(request,'welcome.html',{'name':nm})


def add(request):
    val1 = int (request.POST['num1'])
    val2 = int (request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})
