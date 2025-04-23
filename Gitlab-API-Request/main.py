import requests

response = requests.get("https://gitlab.com/api/v4/users/techworld-with-nana/projects")

list_of_nana_project = response.json()

## Loop through a List to get element one at the time 

for project in list_of_nana_project:
  print(f'{project["name"]}')