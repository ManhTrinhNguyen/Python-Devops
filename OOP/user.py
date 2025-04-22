class User:
  def __init__(self, email, name, password, current_job_title):  
    self.email = email 
    self.name = name 
    self.password = password 
    self.current_job_title = current_job_title

  def change_password(self, new_password):
    self.password = new_password

  def get_usr_info(self):
    print(f"{self.name} - {self.password}")

