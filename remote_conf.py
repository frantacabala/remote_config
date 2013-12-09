#!/usr/local/bin/python


# apt-get install python-nmap
# apt-get install python-paramiko
# apt-get install python-scapy
# apt-get install tcpdump
# apt-get install python-netifaces

import sys
sys.path.append("./lib")
from ssh import *
import paramiko
import getpass
from generate import *
from n_scan import *
from optparse import OptionParser

global SSH_CONNECTION
global IS_CONNECT
	

def clsr():
	os.system("clear")

def ssh_menu(iface,webfolder):
  try:
	global IS_CONNECT
	global SSH_CONNECTION
	print "+---------------------------------------------------"
	print "| Scanning for new computers..."
	scann_port(iface)
	print "| Done!"
	print "+---------------------------------------------------\n\n\n"
	if os.path.exists("/tmp/clients"):
	  c=open_clients("/tmp/clients")
	else:
	  print "No file /tmp/clients - try scan network for new devices"
	for line in c:
	  hw=line.split("-")[0]
	  ip=line.split("-")[1].rstrip('\n')
	  print "+--------------------------------------------------------------------------"
	  print "| Send config script to ====%s --- %s====\t?" % (ip,hw)
	  ans=raw_input("| Send: [y/n]: ")
	  if ans == "y" or ans == "Y":
	    try:
	      print "| ======================="
	      username = raw_input("| Insert your username: ")
	      print "| Connecting...."
	      SSH_CONNECTION = ssh_connect(username,ip)
	      IS_CONNECT=1
	      print "| Sending file..."
	      filename="./remote_conf.py"
	      ssh_send(SSH_CONNECTION,filename)
	      IS_CONNECT=1
	      print "| Done! - file was sended into home folder of connected user..."
	      print "| Disconnecting..."
	      SSH_CONNECTION.close()
	      print "+--------------------------------------------------------------------------\n\n\n"
	    except:
	      print"|"
	  else:
	    print "+--------------------------------------------------------------------------\n\n\n"
	    continue
	c.close()
	print "Upload config scripts done!"
  except KeyboardInterrupt:
    print "|"
  
    	#server = raw_input("Insert servername: ")
    	
    	#ssh_exec_menu(SSH_CONNECTION)
    	#IS_CONNECT=1
    	
    	
	
def generate_config(iface,webfolder):
  print "+---------------------------------------------------"
  print "| Scanning for new computers..."
  scann_port(iface)
  print "| Done!"
  print "+---------------------------------------------------\n\n\n"
  print "Generating config files for all scanned PCs..."
  generate(iface,webfolder)
  print "Done!"
  
def ssh_exec_menu(client):
	global IS_CONNECT
	if IS_CONNECT == 1:	  
	  ssh_execute(client,"l-la")
	  IS_CONNECT=0
   	else:
	  print "You are not connected! Please connect..."

def ssh_send(client,filename):
	global IS_CONNECT
	if IS_CONNECT == 1:	  
	  scp_send(client,filename)
	  IS_CONNECT=0
   	else:
	  print "You are not connected! Please connect..."

def main2():
	parser = OptionParser()
	usage = "usage: %prog [options] arg1 arg2"
	
	parser.add_option("-s","--scan",action="store_true",help="Scann local network for potential computers")
	
	parser.add_option("-U" ,"--upload", action="store_true" ,help="Upload automatic script to PCs")
	
	parser.add_option("-i" , "--interface" , type="string" , dest="interface", help="choose interface - only with option --scan")
	
	parser.add_option("-u", "--username",type="string",dest="username", help="username for login to computer - only with option --connect ")
	
	parser.add_option("-g" , "--generate",action="store_true",help="Generate configuration for all found PCs ")
	
	parser.add_option("-w","--webfolder",type="string",dest="webfolder",help="folder of web server - usually /var/www - need to be pre-configured")
	options, arg = parser.parse_args()
	
	
	if len(arg) == 1:
	  print parser.error("invalid number of arguments")

	  
	  
	if options.scan:
	  if options.interface:
	    print "*************\tscanning network with interface: %s \t*************" % options.interface
	    print "+---------------------------------------------------"
	    scann_port(options.interface)
	    print "+---------------------------------------------------\n\n\n"
	  else:
	    print "missing argument [-i | --interface]"
	    return
	elif options.upload:
	  if options.interface:
	    if options.webfolder:
	      ssh_menu(options.interface,options.webfolder)
	    else:
	      print "missing argument [-w | --webfolder]"
	  else:
	    print "Missing username - use [-i,--interface]"
	    return
	elif options.generate:
	  if options.interface:
	    if options.webfolder:
	      print "*************\tGenerating config files %s \t*************" % options.interface
	      generate_config(options.interface,options.webfolder)
	    else:
	      print "missing argument [-w | --webfolder]"
	  else:
	    print "missing argument [-i | --interface]"


main2()






#client=ssh_connect(username,server)

#output = ssh_execute(client,"ls -la")
