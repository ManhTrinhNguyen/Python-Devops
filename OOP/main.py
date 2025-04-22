from user import User
from post import Post

 # Create Users Object 

tim = User("tim@gmail..com", "Tim", "1234", "Devops")
tim.get_usr_info()

new_post = Post("Some messages", tim.name)
new_post.get_post_info()