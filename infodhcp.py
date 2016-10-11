#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import commands

if sys.argv[1] == "-l":
	concesion = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep '{' |uniq |awk '{print $2}'")
	reserva = commands.getoutput("cat /etc/dhcp/dhcpd.conf |grep host -A2|grep 'fixed-address' |sort |uniq|awk '{print $2}'")
    reserva= reserva.replace(";", "");
	print "Lista de concesiones servidor DHCP"
	print concesion
	print "Lista IP reservadas"
	print reserva

else: 
	concesion = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep -A8 '%s'|grep 'hardware ethernet' |sort |uniq|awk '{print $3}'" % sys.argv[1])
	concesion = concesion.replace(";", "");
	if len(concesion) > 0:
		print "IP;",sys.argv[1]
		print "MAC:",concesion
	else:
		print "No hay ninguna concesión con la ip %s " % sys.argv[1] 


