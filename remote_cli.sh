#!/bin/bash

CONF_FILE="/tmp/my_config.conf"
MAC=` sudo ifconfig eth0 | grep "HW" | tr -s " "|cut -d" " -f5`
RCONF=`echo "$MAC.txt"`
echo $RCONF

#wget -O `echo $CONF_FILE` http://192.168.10.1/$RCONF

wget -O `echo $CONF_FILE` http://192.168.10.1/08:00:27:38:e9:54.txt

IP=`cat /tmp/my_config.conf | grep "IP" | cut -d"-" -f2`
MAC=`cat /tmp/my_config.conf | grep "MAC" | cut -d"-" -f2`
DNS=`cat /tmp/my_config.conf | grep "DNS" | cut -d"-" -f2`
IP=`cat /tmp/my_config.conf | grep "IP" | cut -d"-" -f2`



