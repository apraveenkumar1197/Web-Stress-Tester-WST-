import urllib2,time
import sys
import thread
import time,socket
def Requests_thread(tn,url,fo):
	c=0
	t=0
	tt=0
	tt1=0
	#url=raw_input()
	tim1=time.time();
	#print('| Requests | Time | Thread Name |')
	
	while(1):
		tt=int(time.time())-int(tim1);
		#print(tt)
		try:
			res=urllib2.urlopen('http://'+url).read()
		except KeyboardInterrupt:
			break
		except:
			print('Invalid URL')
			break
		#print(c)
		c=c+1
		if(tt > tt1):
			tt1=tt
			fo.write('\n  '+str(c)+'   |  '+str(tt)+'   |  '+str(tn))
			print('\n  '+str(c)+'   |  '+str(tt)+'   |  '+str(tn))
			c=0

tc=0
tcp=int(input("Enter the Number of Threads : "))
print('Enter the URL [http://www.google.com]\n');
url=raw_input("http://")
print('| Requests | Time | Thread Name |')
fo = open(str(socket.gethostbyname(socket.gethostname())+'_log.txt'), "wb")
while(tc < tcp):	
	thread.start_new_thread(Requests_thread, (tc,url,fo, ))
	tc=tc+1
#Requests_thread(tc,url,fo)
while 1:
   pass