from scapy.all import *
#显示过程
conf.verb=0
ip = input("please enter ip add:")
start_port =int(input("Please input the starting port of the scanned host: "))
end_port = int(input("Please enter the end port of the scanned host:"))
for i in range(start_port,end_port):
	pkt = IP(dst=ip)/TCP(dport=i)
	ans,uans = sr(pkt)
	res = str(ans[0])

	if re.findall("SA",res):
		print(str(i)+"  open")
	else:
		pass