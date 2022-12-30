from django.shortcuts import render

# Create your views here.
def third(request):
    d={'college':'SEAT'}
    return render(request,'third.html',context=d)

def four(request):
    d={'branch':'MECHANICAL'}
    return render(request,'four.html',context=d)