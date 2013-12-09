# Automatic generatorof configuration

from n_scan import get_ip
import os,sys

def open_file(path):
  open(path,'w').close()
  f=open(path,'a+')
  return f

def open_clients(path):
  f=open(path,'r')
  return f
  
def generate(iface,webfolder):
  if os.path.exists("/tmp/clients"):
    c=open_clients("/tmp/clients")
  else:
    print "No file /tmp/clients - try scan network for new devices"
  for line in c:
    
    hw=line.split("-")[0]
    ip=line.split("-")[1]
    print "---- " + hw
    
    user_file=webfolder+hw+".txt"
    conf=create_conf(hw,ip,iface)
    
    user=open_file(user_file)
    user.write(conf)
    user.close()
    
  c.close()  
def create_conf(hw,ip,iface):
  MAC="MAC="+hw+"\n"
  IP="IP="+ip
  DNS="DNS=8.8.8.8\n"
  GW="GW=%s\n" % get_ip(iface)[0]
  MASK="MASK=255.255.255.0"

  return MAC+IP+DNS+GW
  
  