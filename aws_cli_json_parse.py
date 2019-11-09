#!/bin/python36

import subprocess as sb
i=0


sb.getoutput("touch describe-instances_file")
sb.getoutput("aws ec2 describe-instances > describe-instances_file ")


instance_id = "akash"
instance_id_list = []
instance_state = "akash"
instance_state_list = []


while  not instance_id ==  "null":
	instance_id = sb.getoutput("cat describe-instances_file | jq '.Reservations["+str(i)+"].Instances[0].InstanceId'")
	i = i+1
	if not instance_id == "null" :
		instance_id_list.append(instance_id)


i=0
while  not instance_state ==  "null":
	instance_state = sb.getoutput("cat describe-instances_file | jq '.Reservations["+str(i)+"].Instances[0].State.Name'")
	i = i+1
	if not instance_state == "null" :
		instance_state_list.append(instance_state)

i = 0
for id_ in instance_id_list:
	print( id_ + ":" +  instance_state_list[instance_id_list.index(id_)])
	i = i+1
