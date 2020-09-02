from django.shortcuts import render

def home(request):
     #import json
     #import requests

     #api_requests = requests.get("http://dataservice.accuweather.com/currentconditions/v1/540155_PC?apikey=%09sGwdYxLUJfpyoK3coytpzZFXeHU2MfU5&details=true")

     #try:
         #api = json.loads(api_requests.content)
     #except Exception as e:
         #api = "Error..."  

     return render(request, 'home.html', {})  


def Elite_Weather(request):
     return render(request, 'Elite_Weather.html', {})

def Air_Quality(request):
     import json
     import requests

     api_requests = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=18.5204&lon=73.8567&APPID=15s8pr56hh45unlomcn6ub84ei')

     try:
         api = json.loads(api_requests.content)
     except Exception as e:
         api = "Error..."

     return render(request, 'Air_Quality.html', {'api':api})     


def about(request):
    return render(request, 'about.html', {})
