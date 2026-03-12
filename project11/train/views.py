from django.shortcuts import render

# Create your views here.
def listoftrains(request):
    return render(request,'listoftrains.html')