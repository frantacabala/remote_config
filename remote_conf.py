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
from n_scan import *

global SSH_CONNECTION
global IS_CONNECT

def scann_network():
	print "scanning..."
	#try:
	if 1==1:
		loop=1
		while loop == 1:
        		print "Interfaces: "
			iface= get_iface()
			print iface
        		choice = raw_input("insert interface: ")
        		if choice == iface[1] or choice == iface[2] :			
            			#clsr()
            			print "scanning interface '%s'" % choice
				scann_port(choice)
				break
            		else:
				print "Wrong interface! Please again..."
        			continue
    	#except:
        #	print "Something is wrong. Try it again..."
	#	raw_input("\n\nPress enter to continue...")
	

def clsr():
	os.system("clear")

def menu():
	clsr()
	print "+------------------------------------------------+"
	print "| (1) : scann network				"
	print "| (2) : connect to remote machine		"	
	print "| (3) : execute command				"
	print "| (4) : send configuration			"
	print "| (0) : exit application				"
	print "+------------------------------------------------+"

def ssh_menu():
	global IS_CONNECT
	global SSH_CONNECTION
	print "connect to remote machine: "
    	username = raw_input("Inser your username: ")
    	server = raw_input("Insert servername: ")
    	SSH_CONNECTION = ssh_connect(username,server)
    	IS_CONNECT = 1

def ssh_exec_menu():
	global IS_CONNECT
	if IS_CONNECT == 1:
			print "execute command: "
    			command = raw_input("insert command: ")
    			ssh_execute(SSH_CONNECTION,command)
   			IS_CONNECT=0
   	else:
   		print "You are not connected! Please connect..."

def main():
	clsr()
	loop = 1
	choice = 0
	global IS_CONNECT
	IS_CONNECT=0
    	try:
		while loop == 1:
        		menu()
        		choice = raw_input("insert your choice: ")
        		if choice == '1':			
            			#clsr()
            			scann_network()
        		elif choice == '2':
            			#clsr()
            			ssh_menu()
        		elif choice == '3':
        			#clsr()
        			ssh_exec_menu()
        		elif choice == '0':
        			loop = 0
        		else:
        			continue
    	except:
        	pass


main()






#client=ssh_connect(username,server)

#output = ssh_execute(client,"ls -la")
