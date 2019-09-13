#!/bin/python36

import subprocess
from firebase import firebase
p , q = subprocess.getstatusoutput("sudo cat /root/Desktop/Playbook/inventory/selected")
q = q.split('\n')
q.remove(q[0])
print(q)
refrence = firebase.FirebaseApplication('https://ar7778-8c647.firebaseio.com/')
i = 0
request = refrence.delete('user','selected')
for ip in q:
	request = refrence.put('user/selected','IP'+str(i),ip)
	i = i+1

p , q = subprocess.getstatusoutput("sudo cat /root/Desktop/Playbook/inventory/Nselected")
q = q.split('\n')
q.remove(q[0])
print(q)
i = 0
request = refrence.delete('user','Nselected')
for ip in q:
        request = refrence.put('user/Nselected','IP'+str(i),ip)
        i = i+1

p , q = subprocess.getstatusoutput("sudo cat /root/Desktop/Playbook/inventory/al")
q = q.split('\n')
print(q)
i = 0
request = refrence.delete('user','al')
for ip in q:
        request = refrence.put('user/al','IP'+str(i),ip)
        i = i+1

#request = refrence.put('user',"selected",{'ip1':192})

#request = refrence.put('user',"selected",{'ip1':192})

