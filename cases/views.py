from django.shortcuts import render
import os
import json
from django.db.models import Sum
from django.http import HttpResponse,Http404,JsonResponse
from .models import District, DateReport, TestReport

from rest_framework import viewsets
from .serializers import DistrictSerializer



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.

def index(request):
    

    # tempdata()
    d = District.objects.order_by('Confirmed')
    
    t = TestReport.objects.order_by('date').last()
    
    # daily = DateReport.objects.order_by('date').last()
    dr = DateReport.objects.order_by('date')    
    daily = dr.last()
    tc = dr.aggregate(Sum('confirmed'))
    tr = dr.aggregate(Sum('Recovered'))
    td = dr.aggregate(Sum('Death'))
    ta = tc['confirmed__sum'] - tr['Recovered__sum']
    print(daily)
    
    d_active = daily.confirmed - daily.Recovered - daily.Death
    print(d_active)
    
    context = {'d': d , 'dr' : dr , 'tc' : tc, 'ta':ta , 'tr' : tr , 'td': td, 't':t, 'daily':daily , 'da':d_active}

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

    if request.user.is_authenticated:
        # print(vars(request))
        

        dis = District.objects.get(pk=did)
        context = {'d': dis}
        return render(request, 'edit.html', context)
    else:
        return render(request, 'authentication_needed.html')
        # raise Http404("Not logged in")
    

def updated(request,did):

    if request.user.is_authenticated:

        dis = District.objects.get(pk=did)
        dis.Confirmed = request.POST['con']
        dis.Recovered = request.POST['rec']
        dis.Death = request.POST['dea']
        dis.Active = request.POST['act']
        dis.save()
        context = { 'd': dis , 'a': request.POST['con']}
        return render(request, 'update.html', context)

    else:
        return render(request, 'authentication_needed.html')

def tempdata():
    f = open(os.path.join(BASE_DIR,'data.json'))
    data = json.load(f)
    # print(data)
    for i in data:
    # i=data[0]
        d = DateReport()
        
        d.date = i["Date"]
        d.confirmed = i["Confirmed"]
        d.Recovered = i["Recovered"]
        d.Death = i["Death"]
        d.Active = i["Active"]
        d.save()

        print(i)

    f.close()


    fd = open(os.path.join(BASE_DIR,'test.json'))
    data = json.load(fd)
    # print(data)
    for i in data:
    # i=data[0]
        d = TestReport()
        
        d.date = i["Date"]
        d.total_sent = i["TotSent"]
        d.sent = i["Sent"]
        d.total_positive = i["TotPositive"]
        d.new_positive = i["New Positive"]
        d.save()

        print(i)

    f.close()

def data(request):
    return render(request, 'data_upload.html')



def info(request):

    dr = DateReport.objects.order_by('date')    
    daily = dr.last()
    tc = dr.aggregate(Sum('confirmed'))
    tr = dr.aggregate(Sum('Recovered'))
    td = dr.aggregate(Sum('Death'))
    ta = tc['confirmed__sum'] - tr['Recovered__sum']
    d_active = daily.confirmed - daily.Recovered - daily.Death

    a = {
        'tc' : tc['confirmed__sum'], 
        'ta':ta , 
        'tr' : tr['Recovered__sum'] , 
        'td': td["Death__sum"], 
        
     
        'da':d_active

    }

    return JsonResponse(a)




# API

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.order_by('id')
    serializer_class = DistrictSerializer

    http_method_names = ['get']


