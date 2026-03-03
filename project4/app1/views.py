from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def netflix(request):
    return HttpResponse('<h1>vyshu loves sindu</h1>')