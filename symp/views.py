from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render



# Create your views here.
def sympcheck(request):
    app1 = AppIndex.objects.get(pk=1)   
    return render(request, 'symp/sympcheck.html')


    