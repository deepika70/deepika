from django.shortcuts import render

# Create your views here.
def conditional(request):
    d = {'name':'annika', 'age':20}
    return render(request,'conditional.html',d)
def conditional1(request):
    d = {'name':'adwik', 'age':19}
    return render(request,'conditional1.html',d)
def conditional2(request):
    d = {'name':'lucky', 'age':19}
    return render(request,'conditional2.html',d)
def conditional3(request):
    d = {'name':'chinni', 'age':15}
    return render(request,'conditional3.html',d)
    