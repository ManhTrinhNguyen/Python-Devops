import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-west-1")

volumes = ec2_client.describe_volumes(
  Filters=[
    {
      'Name': 'tag:environment',
      'Values': [
        'dev'
      ]
    }
  ]
)['Volumes']


def volume_backup():
  for volume in volumes:
    volume_id = (volume['VolumeId'])
    try:
      new_snapshot = ec2_client.create_snapshot(
        VolumeId=volume_id
      )

      print(new_snapshot)
    except:
      # handle error 
      print('Creating Snapshot went wrong')


# # Scheduler everydays at 1pm
# schedule.every().day.at("13:00").do(volume_backup)



# # To run the Scheduler I have to execute that 
# while True:
#   schedule.run_pending()

volume_backup()