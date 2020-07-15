from django.shortcuts import render
import os

from django.http import HttpResponse,Http404
from .models import District

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# cred = credentials.Certificate(os.path.join(BASE_DIR, 'test-ce84a8a94eca.json'))
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'test-6615.appspot.com'
# })

# bucket = storage.bucket()


# blob = bucket.blob("rsz_20161114_123947-1.jpg")
# print(vars(blob))

# blob.download_to_filename("C:\\Users\\ASUS\\Documents\\covid19\\covid19")

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

    if request.user.is_authenticated:
        print("test")

        dis = District.objects.get(pk=did)
        context = {'d': dis}
        return render(request, 'edit.html', context)
    else:
        return render(request, 'authentication_needed.html')
        # raise Http404("Not logged in")
    

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

