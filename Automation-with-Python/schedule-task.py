import boto3
import schedule

ec2_client = boto3.client('ec2')

ec2_resource = boto3.resource('ec2')

# To get all the Reservations

reservations = ec2_client.describe_instances()

# # Loop through the Reservations to get Reservation
# for reservation in reservations["Reservations"]:
#   # Get Instances
#   instances = reservation['Instances']

#   # Loop through the instances to get instance
#   for instance in instances:
#     # Get Instance ID 
#     instance_id = (instance["InstanceId"])

#     # Get Instance Name 
#     instance_name = (instance["State"]["Name"])

#     print(f"Status of Instance {instance_id} is {instance_name}")


def check_instance_status():
  statues = ec2_client.describe_instance_status(IncludeAllInstances=True)
  for status in statues['InstanceStatuses']:
    instance_status = (status["InstanceStatus"]["Status"])
    system_status = (status["SystemStatus"]["Status"])
    instance_id = status["InstanceId"]
    state = status["InstanceState"]["Name"]
    print(f"Instance {instance_id} status is {state} with status {instance_status}, system status is {system_status}")
  print("#########################################################")

# Every 5 Mininutes execute the check_instance_status
schedule.every(5).minutes.do(check_instance_status)

# Scheduler everydays at 1pm
schedule.every().day.at("13:00").do(check_instance_status)

# To run the Scheduler I have to execute that 
while True:
  schedule.run_pending()

