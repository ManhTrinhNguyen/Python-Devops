import boto3

# Get EC2 Client from us-west-1
ec2_client_us_west_1 = boto3.client('ec2', region_name="us-west-1")

# Get EC2 Resource from us-west-1
ec2_resource_us_west_1 = boto3.resource('ec2', region_name="us-west-1")

reservations_us_west_1 = ec2_client_us_west_1.describe_instances()["Reservations"]

# Create Instance_ID list 
instance_ids_us_west_1 = []

# Iterate through the Reservations 
for reservation in reservations_us_west_1:
  instances = reservation['Instances']
  for instance in instances:
    # Get ID of Instance
    instance_id = instance["InstanceId"]
    instance_ids_us_west_1.append(instance_id)
    

response = ec2_resource_us_west_1.create_tags(
    Resources=instance_ids_us_west_1,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)