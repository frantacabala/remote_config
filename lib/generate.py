# Automatic generatorof configuration

from n_scan import get_ip,get_ip_mask
import os,sys,shutil

def open_file(path):
  open(path,'w').close()
  f=open(path,'a+')
  return f

def open_clients(path):
  f=open(path,'r')
  return f
  
def generate(iface,webfolder):
  count=0
  if os.path.exists("./lib/.clients"):
    c=open_clients("./lib/.clients")
  else:
    print "No file ./lib/.clients - try scan network for new devices"
  for line in c:
    count=count+1
    hw=line.split("-")[0]
    ip=line.split("-")[1]
    print "---- " + hw
    
    user_file=webfolder+hw+".txt"
    conf=create_conf(hw,ip,iface,count)
    
    user=open_file(user_file)
    user.write(conf)
    user.close()
  
  fire_path=webfolder + "firewall"
  shutil.copy2("./lib/.firewall",fire_path)
  c.close()  
def create_conf(hw,ip,iface,count):
  MAC="MAC="+hw+"\n"
  IP="IP="+ip
  DNS="DNS=8.8.8.8\n"
  GW="GW=%s\n" % get_ip(iface)[0]
  MASK="MASK=%s\n" % get_ip_mask(iface)
  HOSTNAME="HOSTNAME=hostPC_%s\n" % count
  

  return MAC+IP+DNS+GW+MASK+HOSTNAME


  