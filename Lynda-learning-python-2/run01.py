import boto3

s3_obj = boto3.resource('s3')
ec2_obj = boto3.resource('ec2')

for i in s3_obj.backets.all():
    print(i.name)
