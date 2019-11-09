#!/bin/python36

import subprocess as sb
i=0
sb.getoutput("touch describe-instances_file")
sb.getoutput("aws ec2 describe-instances > describe-instances_file ")
instance_id = "akash"
instance_id_array = []
while  not instance_id ==  "null":
	instance_id = sb.getoutput("cat describe-instances_file | jq '.Reservations["+str(i)+"].Instances[0].InstanceId'")
	i = i+1
	print(instance_id)
