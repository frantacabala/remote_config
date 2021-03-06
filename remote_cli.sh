#!/bin/bash

CONF_FILE="/tmp/my_config.conf"
FIREWALL="/tmp/my_firewall"
MAC=` sudo ifconfig eth0 | grep "HW" | tr -s " "|cut -d" " -f5`
RCONF=`echo "$MAC.txt"`
echo $RCONF

#wget -O `echo $CONF_FILE` http://192.168.10.1/$RCONF

wget -O `echo $CONF_FILE` http://192.168.10.1/`echo $RCONF`
wget -O `echo $FIREWALL` http://192.168.10.1/firewall


IP=`cat /tmp/my_config.conf | grep "IP" | cut -d"-" -f2`
MAC=`cat /tmp/my_config.conf | grep "MAC" | cut -d"-" -f2`
DNS=`cat /tmp/my_config.conf | grep "DNS" | cut -d"-" -f2`
GW=`cat /tmp/my_config.conf | grep "GW" | cut -d"-" -f2`
MASK=`cat /tmp/my_config.conf | grep "MASK" | cut -d"-" -f2`
HOSTNAME=`cat /tmp/my_config.conf | grep "HOSTNAME" | cut -d"-" -f2`

bash $FIREWALL

