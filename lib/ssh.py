import os,subprocess, getpass
import paramiko

from scp import SCPClient


def ssh_connect(username,server):
	try:
		print "login to server %s@%s..." % (username,server)
		client = paramiko.SSHClient()
		client.load_system_host_keys()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		name = "Enter password for %s@%s :" % (username,server)
		passwd = getpass.getpass(name)
		client.connect(server,username=username,password=passwd)
		print "loged in..."
		raw_input("\nPress enter to continue...")
		return client	
	except:
		print "client does not exist.."
		raw_input("\nPress enter to continue...")

def ssh_execute(client,command):
	stdin,stdout,stderr = client.exec_command(command)
	return stdout.read()

