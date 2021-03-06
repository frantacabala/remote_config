#!/bin/bash

CONF_FILE="/tmp/my_config.conf"
FIREWALL="/tmp/my_firewall"
MAC=` sudo ifconfig eth0 | grep "HW" | tr -s " "|cut -d" " -f5`
RCONF=`echo "$MAC.txt"`

echo "--- LOG Start date: `date` ---"

wget -O `echo $CONF_FILE` http://192.168.10.1/`echo $RCONF` 
wget -O `echo $FIREWALL` http://192.168.10.1/firewall	


IP=`cat /tmp/my_config.conf | grep "IP" | cut -d"=" -f2`
MAC=`cat /tmp/my_config.conf | grep "MAC" | cut -d"=" -f2`
DNS=`cat /tmp/my_config.conf | grep "DNS" | cut -d"=" -f2`
GW=`cat /tmp/my_config.conf | grep "GW" | cut -d"=" -f2`
MASK=`cat /tmp/my_config.conf | grep "MASK" | cut -d"=" -f2`
HOSTNAME=`cat /tmp/my_config.conf | grep "HOSTNAME" | cut -d"=" -f2`



echo "--- Setting up CRON ---"

cat /etc/crontab | grep "rconf_client"
if [ `echo $?` -eq 1 ]; then
        echo "*/1 *       * * *   root    bash /usr/bin/rconf_client &>> /var/log/rconf_client.log" >> /etc/crontab
fi

echo "Done!"

echo "--- Setting up NETWORK ---"
ifconfig eth0 `echo $IP` netmask $MASK

echo "$HOSTNAME" > /etc/hostname

route add default gw `echo $GW` eth0

echo "nameserver $DNS" > /etc/resolv.conf

echo "Done!"

echo "--- Setting up FIREWALL ---"
bash $FIREWALL
echo "Done!"

echo "Set up! - `date` ---"
echo ""
echo ""
echo ""

