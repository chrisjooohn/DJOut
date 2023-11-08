from django.shortcuts import render
from .saveRecord import save
from .portalInit import init
from django.http import HttpResponse

# Create your views here.
def main(request):  
    return render(request, "template/index.html")

def outsystems(request):  
    return render(request, "template/outsystems-portal.html")

def saveRecord(request):    
    return save(request)  

def portalInit(request):    
    return init(request)