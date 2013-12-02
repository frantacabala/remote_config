#!/usr/bin/env python

import sys,nmap, netifaces
from scapy.all import *


def scann_port(ifa):
    	source = '192.168.10.0/24'
	#server_ip=get_ip(ifa)
	ip = get_ip(ifa)
	
    	#try:
	if 1 == 1 :
		ip = get_ip(ifa)
		nm=get_net_addr(ip[0],ip[1])		
		addr="%s/%s" % (nm,ip[1])
		alive,dead=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=addr),iface=ifa, timeout=2, verbose=0)
        	f = open_file()
		print "MAC - IP"
		for i in range(0,len(alive)):
            		client = alive[i][1].hwsrc + "-" + alive[i][1].psrc
			ret=check(f,alive[i][1].hwsrc)			
			if ret != 'true':
				break			
			f.write(client)
			f.write('\n')
			print client
		raw_input("\n\nPress enter to continue...")
		f.close()
   	#except:
        	#pass

def get_net_addr(ip,netmask):
	if netmask >= 24:
		sp= ip.rsplit('.',1)
		new_sp = sp[0]+'.0'		
		return 	new_sp
		
	else:
		sp = ip.rsplit('.',2)
		new_sp = sp[0]+'.0.0'		
		return 	new_sp

def open_file():
	path="/tmp/clients"
	f = open(path,'a+')
	return f
def check(f,hw):
	
	for line in f:
		line= line.split('-',1)
		if line[0] == hw:
			print "This client <%s> exists! Ignore..." % (hw)
			return 'false'
	return 'true'
def get_ip(iface):
	ip = []
	ip.append(netifaces.ifaddresses(iface)[2][0]['addr'])
	ip.append(netifaces.ifaddresses(iface)[2][0]['netmask'])
	ip[1]=sum([bin(int(x)).count('1') for x in ip[1].split('.')])
	return ip

def get_iface():
	return netifaces.interfaces()
