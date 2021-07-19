from django.shortcuts import render
from django.http import HttpResponse
#from ipaddress import *
#from faker import Faker
import random
from .models import Addressing
# Create your views here.
def home(request):
   # faker = Faker()
    ip1=str(random.randint(120,223))
    ip2=str(random.randint(0,255))
    ip3=str(random.randint(0,255))
    ip4=str(random.randint(0,255))
    ip4x=str(random.randint(0,255))
    block= str(random.randint(24,30))
    ip=ip1 + "." + ip2 + "." + ip3 + "." + ip4 
    ipx=ip1 + "." + ip2 + "." + ip3 + "." + ip4x 
    #ip=faker.ipv4()
    x =ip +"/"+block
    obj1=Addressing(ip,block,ip4x)
    classs=obj1.className()
    subnet=obj1.subnet()
    host=obj1.host()
    mask = obj1.mask()
    compare=obj1.IpCompare()
    return render(request,'sim1.html',{'ip':x,'ipx':ipx,'class':classs,'subnet':subnet,'host':host,'mask':mask,'compare':compare})

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    result = val1 + val2
    return render(request,'result.html',{'result':result})

def base(request,name):
    return render(request,'base.html',{'name1':name})