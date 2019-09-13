#!/usr/bin/python36

print("content-type: text/html")
print()

import cgi
import subprocess

mdata = cgi.FieldStorage()
name=mdata.getvalue('ImageN')

if name is not None:
	p , q = subprocess.getstatusoutput("sudo echo \'" + name + "\' | sudo cat > /var/www/cgi-bin/Dcgi/ImageName " )
	print("Successful")
else:
	print("<form action='http://192.168.43.214:/cgi-bin/Dcgi/inputDimage.py'>")
	print("Enter ImageName: <input type='text' name='ImageN'>")
	print("<input type='submit'>")
	print("</form>")

