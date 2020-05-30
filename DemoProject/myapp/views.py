from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests
import json

def hello(request):
    #return HttpResponse("<h1>Hellooo...</h1>")
    url = "https://api.covid19api.com/summary"

    headers = {
            "cache-control": "no-cache"
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)
    y=json.loads(response.text)
    #for i in y: 
    x=y['Countries']
    world=y['Global']

    return render(request,"home.html",{"vaibhav" : x,"global" : world})

def getContrysData(request):
    url = "https://api.covid19api.com/summary"

    headers = {
            "cache-control": "no-cache"
    }

    response = requests.request("GET", url, headers=headers)
    y=json.loads(response.text)
    #for i in y: 
    print(y['Countries']) 
    
    return HttpResponse(y, content_type='application/json')

