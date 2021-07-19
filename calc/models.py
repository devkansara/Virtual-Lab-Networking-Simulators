from django.db import models

# Create your models here.
class Addressing:
    def __init__(self,ip,block,ipx):
        self.ip=ip
        self.block=block
        self.ipx=ipx
    
    def className(self):
        netId=int(self.ip.split('.')[0])
        if (netId < 128):
            return "Class A"
        elif (netId <192):
            return "Class B"
        elif (netId <224):
            return "Class C"
        elif (netId <240):
            return "Class D"
        elif (netId <256):
            return "Class E"
        else:
            return "Sachin"
    
    def subnet(self):
        netId=int(self.ip.split('.')[0])
        if (netId < 128):
            sub=int(self.block)-8
            subnet=2 ** sub
            return subnet
        elif (netId <192):
            sub=int(self.block)-16
            subnet=2 ** sub
            return subnet
        elif (netId <224):
            sub=int(self.block)-24
            subnet=2 ** sub
            return subnet
    
    def host(self):
            sub=32-int(self.block)
            subnet=(2 ** sub)-2
            return subnet
    
    def mask(self):
        block=int(self.block)
        mask=str(1)
        for i in range(1,block):
            mask=mask+str(1)

        for i in range(32-block):
             mask=mask+str(0)

        ip1=mask[0:8]
        ip2=mask[8:16]
        ip3=mask[16:24]
        ip4=mask[24:32]

        ip11=str(self.BinaryToDecimal(ip1))
        ip22=str(self.BinaryToDecimal(ip2))
        ip33=str(self.BinaryToDecimal(ip3))
        ip44=str(self.BinaryToDecimal(ip4))

        submask = ip11 + '.' + ip22 + '.' + ip33 + '.' + ip44
        return submask


    def BinaryToDecimal(self,binary):
        decimal = 0
        for digit in binary:
            decimal = decimal*2 + int(digit)
        return decimal

    def IpCompare(self):
        hostId=self.host()+2
        x=int(self.ip.split('.')[-1])//hostId
        netId=x*hostId
        brodId=netId+hostId-1
        if((int(self.ipx) < brodId) and (int(self.ipx) > netId)):
            return "YES"
        else:
            return "NO"



