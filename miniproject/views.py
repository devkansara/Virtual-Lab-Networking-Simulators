from django.shortcuts import render
from django.http import HttpResponse
#from ipaddress import *
#from faker import Faker
import random
from .models import Addressing
# Create your views here.

def sim(request):
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
    return render(request,'sim1.html',{'title':"Simulation",'ip':x,'ipx':ipx,'class':classs,'subnet':subnet,'host':host,'mask':mask,'compare':compare})


def mainpage(request):
      return render(request,'mainpage.html',{'title':"IPv4 Subnetting"})

def firstpage(request):
      return render(request,'firstpage.html',{'title':"Virtual Labs"})

#dev
def simpleparitycheck(request):
	n1=request.GET.get('inputdata')
	#n1 = int(input("enter input data"),2)	
	n = str(n1)
	one_count = 0
	onecount=0
	tnum=0
	p=0
	for i in n:
		if i == "1":
			one_count+=1
			onecount= one_count
	if(onecount % 2 != 0):
		p=1
		tnum= n + '1'
	else:
		p=0
		tnum= n + '0'

	oc=0
	for j in tnum:
		if j == "1":
			oc+=1
	if(oc % 2  == 0):
		res="No Error Found"
	else:
		res="Error Found"
	
	return render(request, 'simpleparitycheck.html', {'actualparity':p, 'datatransmitted':tnum, 'actualoutput':res, 'onecountres':oc})

def experiment2(request):
    return render(request, 'experiment2.html')