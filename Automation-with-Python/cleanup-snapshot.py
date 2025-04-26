import boto3 
from operator import itemgetter
import schedule

ec2_client = boto3.client('ec2', region_name = "us-west-1")

snapshots = ec2_client.describe_snapshots(
  OwnerIds=['self']
)['Snapshots']


sort_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)

# Instead of iterate to the whole list I want to skip the first 2 elements 
def cleanup_snapshot():
  for snapshot in sort_by_date[2:]:
    print(snapshot['StartTime'])
    print(snapshot['SnapshotId'])
    # Delete Snapshot 

    response = ec2_client.delete_snapshot(
      SnapshotId=snapshot['SnapshotId']
    )

    print(response)


# Scheduler everydays at 1pm
schedule.every().day.at("13:00").do(cleanup_snapshot)

# To run the Scheduler I have to execute that 
while True:
  schedule.run_pending()