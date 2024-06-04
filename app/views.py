from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    da=datetime.datetime.now()
    d={'data':'hai PyTHon How aRe yOU','da':da,'c':10}
    return render(request,'filter.html',d)

def userfilters(request):
    d={'data':'hai PyTHon How aRe yOU'}
    return render(request,'userfilter.html',d)