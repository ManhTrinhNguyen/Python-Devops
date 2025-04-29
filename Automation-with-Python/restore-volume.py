import boto3 
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name='us-west-1')
ec2_resource = boto3.resource('ec2', region_name='us-west-1')

# Get Instance ID from the UI
instance_id = "i-0c7270f4c6bb9b931"

# Get Snapshot that I created for volume associated with this Instance

# 1. Get Volumes of EC2 Instances 

volumes = ec2_client.describe_volumes(
  Filters = [
    {
      'Name': 'attachment.instance-id',
      'Values': [instance_id]
    }
  ]
)

instance_volume = volumes['Volumes'][0]

# 2. Get Snapshots of Volumes 

snapshots = ec2_client.describe_snapshots(
  OwnerIds=['self'],
  Filters=[
    {
      'Name': 'volume-id',
      'Values': [volumes['Volumes'][0]['VolumeId']]
    }
  ]
)['Snapshots']

latest_snapshot = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)[0]


# 3. Create Volume from Snapshot 
# This woule create a new volume from the Snapshot in the AZ of the Instance and add following tag to that new volume
new_volume =  ec2_client.create_volume(
  SnapshotId=latest_snapshot['SnapshotId'],
  AvailabilityZone="us-west-1a",
  TagSpecifications=[
    {
      'ResourceType': 'volume',
      'Tags': [
        {
          'Key': 'Name',
          'Value': 'dev'
        }
      ]
    }
  ]
)

# Attach Volume to EC2 Instance 
# This way I can address at specific Instance, I don't have to iterate and get IDs
# Device value can be something like from my existing volume, can't be the same value bcs I attached this volume to the same Instance
# If I execute it  I have a little issue which is timing, basically the new volume get created right after I am trying to attach it to EC2 Instance and for a volume to be able to attach to an instance it have to be in an available state
# To fix the timing issue between these 2 function execution so I want to wait to allow volume get created and become available and then try to attach that volume
# I will check the Status of Volume until it become available by using While loop 

while True:
  volume = ec2_resource.Volume(new_volume['VolumeId'])
  print(volume.state)
  if volume.state == 'available':
    ec2_resource.Instance(instance_id).attach_volume(
    VolumeId=new_volume['VolumeId'],
    Device='/dev/xvdb'
  ) 
    break



