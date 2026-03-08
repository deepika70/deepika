from django.shortcuts import render
[]
# Create your views here.

def jingaprint(request):
    d={'name':'deepu','age':18}
    return render(request,'jingaprint.html',context=d)