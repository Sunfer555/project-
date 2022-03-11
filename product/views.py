from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def ok(request):
    return render(request,'ok.html')
