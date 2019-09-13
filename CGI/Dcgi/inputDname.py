#!/usr/bin/python36

print("content-type: text/html")
print()

import cgi
import subprocess

mdata = cgi.FieldStorage()
name=mdata.getvalue('Dname')

if name is not None:
	p , q = subprocess.getstatusoutput("sudo echo \'" + name + "\' | sudo cat > /var/www/cgi-bin/Dcgi/Dname " )
	print("Successful")
else:
	print("<form action='http://192.168.43.214:/cgi-bin/Dcgi/inputDname.py'>")
	print("Enter DockerName: <input type='text' name='Dname'>")
	print("<input type='submit'>")
	print("</form>")

