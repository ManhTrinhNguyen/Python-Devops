import boto3

ec2_client = boto3.client('ec2')

all_available_vpc = ec2_client.describe_vpcs()

print(all_available_vpc["Vpcs"][0]["VpcId"])