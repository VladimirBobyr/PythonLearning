import boto3

s3_obj = boto3.resource('s3')
#ec2_obj = boto3.resource('ec2')
#iam_obj = boto3.resource('iam')

for each in s3_obj.buckets.all():
    print(each.name)