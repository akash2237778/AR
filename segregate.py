#!/usr/bin/python36


import subprocess

listIP = []
ipS1 = []
ipS2 = []

s , n = subprocess.getstatusoutput("sudo echo \"[Nselected]\" | cat > /root/Desktop/Playbook/inventory/Nselected")
s , n = subprocess.getstatusoutput("sudo echo \"[selected]\" | cat > /root/Desktop/Playbook/inventory/selected")
p , q = subprocess.getstatusoutput("sudo ls /root/Desktop/Playbook/sIP/ | grep 192")
q = q.split("\n")
listIP = q
print(listIP)

for ip in listIP :
	p , q = subprocess.getstatusoutput("sudo cat /root/Desktop/Playbook/sIP/"+ip)
	if q == "2":
		ipS1.append(ip)
		m , content = subprocess.getstatusoutput("sudo cat /root/Desktop/Playbook/inventory/Nselected")
		if not ip in content :
			s , n = subprocess.getstatusoutput("sudo echo \""+ip+"\" | cat >> /root/Desktop/Playbook/inventory/Nselected")
	elif q == "1":
		ipS2.append(ip)
		m , content = subprocess.getstatusoutput("sudo cat /root/Desktop/Playbook/inventory/selected")
		if not ip in content :
			s , n = subprocess.getstatusoutput("sudo echo \""+ip+"\" | cat >> /root/Desktop/Playbook/inventory/selected")


print(ipS1)
print(ipS2)
