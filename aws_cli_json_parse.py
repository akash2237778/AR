#!/bin/python36

import subprocess as sb
i=0


sb.getoutput("touch describe-instances_file")
sb.getoutput("aws ec2 describe-instances > describe-instances_file ")


instance_id = "NullValue"
instance_id_list = []
instance_state = "NullValue"
instance_state_list = []
instance_name = "NullValue"
instance_name_list =[]

while  not instance_id ==  "null":
	instance_id = sb.getoutput("cat describe-instances_file | jq '.Reservations["+str(i)+"].Instances[0].InstanceId'")
	i = i+1
	if not instance_id == "null" :
		instance_id_list.append(instance_id)


i=0
while  not instance_name ==  "null":
	instance_name = sb.getoutput("cat describe-instances_file | jq '.Reservations["+str(i)+"].Instances[0].Tags[0].Value'")
	i = i+1
	if not instance_name == "null" :
		instance_name_list.append(instance_name)
		#instance_name_list[i] = instance_name

i=0
while  not instance_state ==  "null":
	instance_state = sb.getoutput("cat describe-instances_file | jq '.Reservations["+str(i)+"].Instances[0].State.Name'")
	i = i+1
	if not instance_state == "null" :
		instance_state_list.append(instance_state)

sb.getoutput("rm /var/www/html/aws_info.csv")
sb.getoutput("touch /var/www/html/aws_info.csv")
i = 0
for id_ in instance_id_list:
	describe=id_ + "," +  instance_state_list[instance_id_list.index(id_)] + "," + instance_name_list[instance_id_list.index(id_)] + "\n"
	i = i+1
	sb.getoutput("echo " + describe +  " | cat >> /var/www/html/aws_info.html")


