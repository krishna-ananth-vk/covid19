from django.shortcuts import render

from django.http import HttpResponse,Http404
from .models import District

# Create your views here.

def index(request):


    d = District.objects.order_by('id')
    context = {'d': d}

    return render(request, 'index.html', context)
    # return HttpResponse('hello world')
def districtwise(request,did):
    try:
        dis = District.objects.get(pk=did)
    except District.DoesNotExist:

        raise Http404("No data available")
        


    context = {'d': dis}
    return render(request, 'district.html', context)

def edit(request,did):
    dis = District.objects.get(pk=did)
    context = {'d': dis}
    return render(request, 'edit.html', context)
    

def updated(request,did):

    dis = District.objects.get(pk=did)
    dis.Confirmed = request.POST['con']
    dis.Recovered = request.POST['rec']
    dis.Death = request.POST['dea']
    dis.Active = request.POST['act']
    dis.save()
    context = { 'd': dis , 'a': request.POST['con']}
    return render(request, 'update.html', context)


def login(request):
    pass

