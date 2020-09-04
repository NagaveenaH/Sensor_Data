from django.shortcuts import render
from django.http import HttpResponse
from .models import store_extract
import requests
import schedule
import time
from pymongo import MongoClient
# Create your views here.
def home(request):  
    insert_data(request)
    return render(request,'index.html');


def insert_data(request):   
    url='https://openweathermap.org/data/2.5/weather?q=London,uk&appid=439d4b804bc8187953eb36d2a8c26a02&units=matric'
    result=requests.get(url).json()
    
    sensor_data={
    'Temprature': {'reading':result['main']['temp'], 'timestamp':result['dt'], 'sensorType':'temprature'},
    'Pressure': {'reading':result['main']['pressure'], 'timestamp':result['dt'], 'sensorType':'pressure'},
    'Humidity':{'reading':result['main']['humidity'], 'timestamp':result['dt'], 'sensorType':'humidity'},                   
    }
    store_extract.objects.create(reading = sensor_data['Temprature']['reading'], timestamp=sensor_data['Temprature']['timestamp'], sensor_type=sensor_data['Temprature']['sensorType']) 
    store_extract.objects.create(reading = sensor_data['Pressure']['reading'], timestamp=sensor_data['Pressure']['timestamp'], sensor_type=sensor_data['Pressure']['sensorType']) 
    store_extract.objects.create(reading = sensor_data['Humidity']['reading'], timestamp=sensor_data['Humidity']['timestamp'], sensor_type=sensor_data['Humidity']['sensorType']) 
     
    #return render(request,'index.html')

def fetch_data(sensorType):
    #Temp=store_extract.objects.filter(sensor_type='temprature').values()
    Temp=store_extract.objects.filter(sensor_type=sensorType).values()
    # print(Temp)  
    for i in range(len(Temp)):
        del Temp[i]['id'] 
    List=[i['reading'] for i in Temp]
    Min=min(List)
    Max=max(List)   
    Mean=sum(List)/len(List)
    return Temp,Min,Max,Mean

def getSensorType(request):    
    stype=request.POST["sensortype"]
    if stype=="temp":
        Temprature,Min,Max,Mean=fetch_data('temprature')
        #print('python_js',Temprature)
        return render(request,'index.html',{'result':Temprature,'Min':Min,'Max':Max,'Mean':Mean});
    elif stype=="humidity":
        Humidity,Min,Max,Mean=fetch_data('humidity')
        #print('python_js',Humidity)
        return render(request,'index.html',{'result':Humidity,'Min':Min,'Max':Max,'Mean':Mean});
    elif stype=="pressure":
        Pressure,Min,Max,Mean=fetch_data('pressure')
        #print('python_js',Pressure)
        return render(request,'index.html',{'result':Pressure,'Min':Min,'Max':Max,'Mean':Mean});
    return render(request,'index.html',{'result':"Select temperature"});
    
 
              
        
       
             
     