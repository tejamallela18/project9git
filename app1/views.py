from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'NAGATEJA'}
    return render(request,'first.html',context=d)

def second(request):
    d={'mobile':6304542125}
    return render(request,'second.html',context=d)