#!/usr/bin/python36

print("content-type: text/html")
print()

import cgi
import subprocess

mdata = cgi.FieldStorage()
ip=mdata.getvalue('ip')

print(ip)
p , q = subprocess.getstatusoutput("sudo touch /root/Desktop/Playbook/inventory/al")
print(p)
p , q = subprocess.getstatusoutput("sudo chmod 0777 /root/Desktop/Playbook/inventory/al")
print(p)
p , q = subprocess.getstatusoutput("sudo touch /root/Desktop/Playbook/sIP/"+ip)
print(p)
p , q = subprocess.getstatusoutput("sudo chmod 0777 /root/Desktop/Playbook/sIP/"+ip)
print(p)

p , check = subprocess.getstatusoutput("sudo cat /root/Desktop/Playbook/sIP/"+ip)
print("CAT IP")
print(check)

if check == "1" :
	print("Hello")
	p , q = subprocess.getstatusoutput("sudo echo \"2\" | sudo  cat > /root/Desktop/Playbook/sIP/"+ip)	
elif check == "2" :
	p , q = subprocess.getstatusoutput("sudo echo \"1\" | sudo  cat > /root/Desktop/Playbook/sIP/"+ip)	
elif check == "0" :
	p , q = subprocess.getstatusoutput("sudo echo \"1\" | sudo  cat > /root/Desktop/Playbook/sIP/"+ip)	
else :
	p , q = subprocess.getstatusoutput("sudo echo \""+ip+"\" | sudo  cat >> /root/Desktop/Playbook/inventory/al")
	p , q = subprocess.getstatusoutput("sudo echo \"0\" | sudo  cat > /root/Desktop/Playbook/sIP/"+ip)	

p , q = subprocess.getstatusoutput("sudo /root/Desktop/Playbook/segregate.py")



##print(q)
##p , q = subprocess.getstatusoutput("sudo ansible-playbook /root/Desktop/Playbook/Dpackage.yml")
##print(p)
