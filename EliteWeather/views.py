from django.shortcuts import render

def home(request):
     #import json
     #import requests

     #api_requests = requests.get("http://dataservice.accuweather.com/currentconditions/v1/540155_PC?apikey=%09sGwdYxLUJfpyoK3coytpzZFXeHU2MfU5&details=true")

     #try:
         #api = json.loads(api_requests.content)
     #except Exception as e:
         #api = "Error..."

     return render(request, 'home.html', {})   # {'api':api}


def Elite_Weather(request):
    return render(request, 'Elite_Weather.html', {})


def about(request):
    return render(request, 'about.html', {})
