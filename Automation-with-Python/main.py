import boto3

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

all_available_vpc = ec2_client.describe_vpcs()

vpcs = all_available_vpc["Vpcs"] # Get Vpcs array

# I will loop through the Vpcs array to get a single vpc . The
for vpc in vpcs:
  # Get vpc_id 
  print(vpc["VpcId"])

  # Get CidrBlockAssociationSet array 
  cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]

  # Loop through cidr_block_assoc_sets  
  for assoc_set in cidr_block_assoc_sets:
    print(assoc_set["CidrBlock"])



# Create VPC 

# This will return VPC resource . Give a resource Object back so we can use it for subsequent call 

new_vpc = ec2_resource.create_vpc(
  CidrBlock = "10.0.0.0/16"
) 
  
new_vpc.create_subnet(
  CidrBlock = "10.0.1.0/24"
)

new_vpc.create_subnet(
  CidrBlock = "10.0.2.0/24"
)

new_vpc.create_tags(
  Tags = [
    {
      'Key': 'Name',
      'Value': 'my-vpc'
    }
  ]
)