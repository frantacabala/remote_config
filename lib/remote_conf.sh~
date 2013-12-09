#!/bin/bash

CONF_FILE="/tmp/my_config.conf"
MAC=` sudo ifconfig eth0 | grep "HW" | tr -s " "|cut -d" " -f5`
RCONF=echo "$MAC.txt"

wget -O `echo $CONF_FILE` http://192.168.10.1/$RCONF



