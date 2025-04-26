import boto3 

client = boto3.client('eks', region_name = 'us-west-1')

clusters = client.list_clusters()['clusters']

for cluster in clusters:
  response = client.describe_cluster(name = cluster)
  cluster_status = response['cluster']['status']
  cluster_endpoint = response['cluster']['endpoint']
  cluster_version = response['cluster']['version']

  print(cluster_status)
  print(cluster_endpoint)
  print(cluster_version)