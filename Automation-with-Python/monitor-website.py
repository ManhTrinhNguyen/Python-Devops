import requests
import smtplib
import os
import paramiko
from fabric import Connection


# Access the application 
# This will give me an response

EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_notifications(msg):
  with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
      smtp.starttls()
      smtp.ehlo()
      smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
      smtp.sendmail(EMAIL_USERNAME, EMAIL_USERNAME, msg)

try:
  response = requests.get('http://50-116-2-196.ip.linodeusercontent.com:8080/')

  # I want to check if the Application accessible and it actually giving back status code 200 

  if False:
    print("Application is up and running successfully")
  else: 
    print("Application downs. Fix it")
    
    # Send email to me 
    msg = f"Subject: SITE DOWN\n Application return {response.status_code}. Fix the issue! Restart the Application"
    send_notifications(msg)

    # Restart Application
    ssh = Connection(
      host='50.116.2.196',
      user='root',
      connect_kwargs={
          "key_filename": "/Users/trinhnguyen/.ssh/id_rsa"
      }
    )
    result = ssh.run('docker ps', hide=True)
    print(result.stdout)

except Exception as ex:
  print('Connection error happen')
  print (ex)
  # Send email to me 
  msg = f"Subject: SITE DOWN\n Application not accessible at all !!!"
  send_notifications(msg)
