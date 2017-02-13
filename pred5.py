
import numpy as np
import matplotlib.pyplot as plt

import sys
import os

#first generate some datapoint for a randomly sampled noisy sinewave
#x = np.random.random(1000)*10
#noise = np.random.normal(scale=0.3,size=len(x))
#y = np.sin(x) + noise


count =0
alpha=0.5
import json
 
x1=[]
y1=[]
f = open('try1.json')
data = json.load(f)
for key in data.keys(): 
	print key
	x1.append(int(key))
	count+=1

print x1


for key,value in data.items():
	print value
	y1.append(int(value))

print y1
        	
x=np.array(x1).astype(np.float)
print x
y=np.array(y1).astype(np.float)
print y

print count
sum1=0
print "For the next time unit the CPU Usage is: "
c=alpha*((y[count-2]+y[count-1])/2)+(1-alpha)*y[count-1]
print c
for i in range(0,count):
	sum1=y[i]+sum1
avg=sum1/count
print avg

if (c>avg):
	print "scale up"
	if (c>(avg+.5) and c<(avg+1.0)):
		n=1
		print n
	elif(c>(avg+1.0) and c<(avg+1.5)):
		n=2
		print n
	elif(c>(avg+1.5)):
		n=3
		print n
	else:
		print("too many nodes to scale")
	f=open("a.txt","w+")
	f.write("%d" % (n))
	f.close()
	print "Number of nodes = ",n
	os.system('MY_VAR=%d vagrant up' % (n))
	

elif (c<avg):
	print "scale down"
	if((avg-c)<=1):
		t=1
	elif((avg-c)<=2 and (avg-c)>1):
		t=2
	elif((avg-c)<=3 and (avg-c)>2):
		t=3
	else:
		print("too many nodes to scale")

	print "Scaling down."
	x=t
	buff=[]
	str1='[master]'
	str2='[nodes]'
	fl=0
	text= open("/home/krutika/vm-an1/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory","r")
	for line in text:
		for word in line.split():
			if(word==str1):
				fl=1
			if(word==str2):
				fl=0
			if(fl==1):
				buff.append(word)
	text.close()
	f=open("a.txt","r")
	c=int(f.read())
	b=int(c)
	f.close()
	print buff
	while(x!=0):
		fl=0
		if(b==len(buff)-1):
			print "No more VMs can be destroyed. Exiting."
			break
		str3='node%d' % (c)
		for i in range(1,len(buff)):
			w=buff[i]
			if str3 in w:
				print "Can't destroy master node. Moving on."
				fl=1
		if(fl==0):
			os.system('MY_VAR=%d vagrant destroy node%d -f' % (b,c))
			b=b-1
			x=x-1
		c=c-1
	f=open("a.txt","w")
	f.write("%d" % (b))
	f.close()
	


else: 
	print "dont scale"

#plot the data
plt.plot(x,y,'ro',alpha=0.5,ms=4,label='data')
plt.xlabel('Time')
plt.ylabel('CPU Usage')

def weighted_moving_average(x,y,step_size=0.05,width=1):
    bin_centers  = np.arange(np.min(x),np.max(x)-0.5*step_size,step_size)+0.5*step_size
    bin_avg = np.zeros(len(bin_centers))

    #We're going to weight with a Gaussian function
    def gaussian(x,amp=1,mean=0,sigma=1):
        return amp*np.exp(-(x-mean)**2/(2*sigma**2))

    for index in range(0,len(bin_centers)):
        bin_center = bin_centers[index]
        weights = gaussian(x,mean=bin_center,sigma=width)
        bin_avg[index] = np.average(y,weights=weights)

    return (bin_centers,bin_avg)

#plot the moving average
bins, average = weighted_moving_average(x,y)
plt.plot(bins, average,label='weighted moving average')

plt.show()




