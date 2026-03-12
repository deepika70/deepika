from django.shortcuts import render

# Create your views here.
def listofbusses(request):
    return render(request,'listofbusses.html')