- [Automation with Python (Spreadsheet)](#Automation-with-Python)

- [OOP](#OOP)

- [Project: API Request to GitLab ](#Project-API-Request-to-GitLab)

- [Boto Library (AWS SDK for Python)](#Boto-Library-AWS-SDK-for-Python)

- [Terraform vs Python When to use which tool](#Terraform-vs-Python-When-to-use-which-tool)

- [Health Check EC2 Status Check](#Health-Check-EC2-Status-Check)

- [Scheduling the Status Checks](#Scheduling-the-Status-Checks)

- [Configure Server Add Environment Tags to EC2](#Configure-Server-Add-Environment-Tags-to-EC2)

- [Print EKS Cluster Info](#Print-EKS-Cluster-Info)

- [Automate backup for EC2 Instances](#Automate-backup-for-EC2-Instances)

- [Automate cleanup of old Snapshot](#Automate-cleanup-of-old-Snapshot) 

- [Automate cleanup of old Snapshot multiple Volumes](#Automate-cleanup-of-old-Snapshot-multiple-Volumes)

- [Automate restoring EC2 Volume from the Backup](#Automate-restoring-EC2-Volume-from-the-Backup)

- [Boto3 Documents](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

- [Hanlding Error](#Hanlding-Error)

- [Website Mornitoring](#Website-Mornitoring)

    - [Create Server and run Nginx container](#Create-Server-and-run-Nginx-container) 

# Python-Devops

## Automation 

Python has many greate Library to automate Devops task from CI/CD Pipelines to Cloud Platform and Monitoring . 

I can write python script to do automated backups cleanups on the Servers 

I can also just general tasks with Python, like when working with Excel sheets or automating some task on my Laptop  

#### Why do I need Python as a Devops Engineer ?

I am as a Devops engineer will be working with many different tools and trying to combine them . For example : 

    Automatically update Jira ticket information after Jenkins build has run suncess . 
    
    Or Automatically trigger Jenkins jobs on some events that happen during software development process, sending notification to write team member on specific events when something happens in the system 

    Doing regular backups for my Nexus or Jenkins servers or Application DB. 
    
    Cleaning up all Docker images from servers to free up Server space

    In addition to that I may need to create automation scripts or small programs for my team, for developers and testers and operations to solve some of their problems 

#### Python interpreter 

Python interpreter is basically a program that know how to execute Python code, it will know how to interpret or translate my Python code into instructions that computer can understand 


#### Python IDE vs Simple File Editor 

Whenever I am working with tools like Pycharm have all the functionality that I need to write code and then execute code I basically have everything in one place, whenever we write we can execute or run right away 

Without tool like that how would I write code and to execute that code ? -> I can do that by `python3 <python-file>` in the terminal 

IDE (Intergrated Development Environment) I have everything in one place, I don't need to use Terrminal . 

With IDE I also have syntax highlighting errors or code sunggestion etc ... 

## Strings and Number Data Type 

First concept in programing language is `Data Type`

Data type for text called `String` 

Data type for number called: 

 - `Interger` : Whole number, possitive or negative

 - `Float` : contain number with decimals

#### Working with Numbers 

I can do any Math Operation on numbers in Number in Programming Languges (Python, ...) : `+`, `-`, `*`, `/`

!!! NOTE : If I am doing Web Dev or maybe Devops Automations, I don't need to be Math genius for that 

#### String Concatenation 

String Concatenation is for combining multple Strings 

For example : `print(f"20 days are {20 * 24 * 60} minutes")` . 

#### Varibles 

```
to_seconds = 24 * 60 * 60

print (f"20 days are {to_second} seconds")
```

!!! NOTE: In Python, defining a Variables or giving values for it, syntaxs are very simple compare to other Languages . 

!!! NOTE : Naming convention or standared for Variables by using `_` 

In Python there are some specific words that have special meaning to Python, these are called reserved words, So I can't use these words as `variable` names 

**Best practice** : Name `variable` so me later and also othe programmers who are working with me understande what this is 

## Function 

`Variable` is to avoid duplication for specific values 

`Function` is to avoid duplication for the whole line, whole pices of code with multiple different stuff in it

`Function` are blocks of code does something more complex that is again used in order to avoid repeating the same logic or most of the same logic in my code 

```
to_seconds = 24 * 60 * 60

def hello_word ():

    print("Hello World")

def days_to_units():
    print(f"20 days are {to_seconds} seconds")
```

#### Function Parameters 

Information can be passed into function aas Parameters

Parameters are also called Arguments 

To define parameters by using `variable`, I can call it whatever I want 


```
to_seconds = 24 * 60 * 60

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {to_seconds} seconds")

days_to_units(35)
```

`Function` help reduce code duplication, more descriptive

## Accepting User Input

To write a program that ask for and accepts a user input and then  then does some kind of caculation or logic base on that user input by using `input()`

`input()` will give user a prompt to enter some input value

`input()` is acutally a function that Python provided with 

I can do is in `input()` I can provide a parameter that tell a user something like enter a values for something 

`\n` make into a new line 

To use a value of the function by assigning whatever result `input()` usage give me, I want to save that value into a `variable` that I can access it later

```
to_seconds = 24 * 60 * 60

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {to_seconds} seconds")

user_input = input("Hey user enter a number of days\n")
```    

`input()` always return string 

#### Function with return value 

`function` can return data as a result

Turning a value from data type to another called `Casting`

```
to_seconds = 24 * 60 * 60

def days_to_units(num_of_days):
    return f"{num_of_days} days are {to_seconds} seconds"

user_input = input("Hey user enter a number of days\n")

user_input_number = int(user_input) # Make user input into a number

calculated = days_to_units(user_input_number)

print (calculated)
```

## Error Handling with Try-Except 

The `try...except`  block in Python is used to handle errors (exceptions) gracefully so that your program doesn’t crash when something goes wrong.

```
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

```
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
```

## While Loop 

The while loop in Python is used to repeat a block of code as long as a condition is True.

```
while condition:
# code to repeat
```

```
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1
```

= Output 

```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

## List and For loops 

A list is a collection of items, ordered and changeable. You create one using square brackets `[]`.

A for loop lets you go through each item in a list:

```
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

```

= Output 

```
apple
banana
cherry
```

## Sets 

A set is an unordered, unindexed collection of unique elements.

Set is a list of elements with unique values inside 

Does Not allow duplicate values 

```
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}
```

To convert List into a set: `set()`

```
fruits = ["apple", "banana", "cherry"]

set(fruits)
```

<img width="499" alt="Screenshot 2025-04-22 at 10 18 52" src="https://github.com/user-attachments/assets/fc2325a6-2954-4fa2-bf0f-4a41d61ec0c7" />

## Dictionary Data Type 

More complex data structure that groups multiple
simple data types together

Stores data values in key:value pairs

Duplicates are not allowed

```
person = {
    "name": "Trinh",
    "age": 26,
    "country": "USA"
}
```

```
person = {"name": "Trinh", "age": 26, "job": "DevOps"}

# Keys only
for key in person:
    print(key)

# Keys + values
for key, value in person.items():
    print(key, "→", value)
```
    
## Modules

Logically organize Python code 

Module should contain related code 

If I have multiple Python file in the Project .To connect them together by using concept called `Modules`

`Modules` is a Python file that contains functions or variables that I can use in another Python file . 

 Any Python file that I have in my Project both of these are `modules` and I can reference one module from another . The idea is I can structure my Application using `modules`

## Packages, PyPI and pip 

#### Build-in and Third Party 

When I install Python it comes with a set of `modules` that are `built-in` into Python 

However there are many more `modules` for other diffent use cases like Web dev, ML .... I need to install as I needed 

Python Modules live in module Repositoy called `pypi` 

#### Module vs Package 

Module is a Python file that has a name of that file . Module is 1 Python file that contain all these function and variable that I can use 

Package is a collection of module . Contain multiple 
Python file . Package alway has `__init__.py` file, and this file differentiates a normal folder with bunch of Python files from an actual package with Python files 

#### Pip 

To install package locally so that I can use it in my Project . In Python I install packages using a Package Manager tool called `pip`

`pip` is a package manager for Python . Every programming languge has its own Package Manager tool

One of the main task of `pip` is to install external packages or libraries or also called dependencies for my Project  


In Python version 3 when I intall Python, Python installed `pip` come with it 

## Automation with Python

#### Introduction 

I will write an Application that will write a Spreadsheet file from my local file system

This could be a useful use case if I am working with lots of files and I want to do some data processing in those files and I don't want to do that manually by automating or writing a program in Python that basically can do anything in a file or accress multuple files 

#### Exercise 

I will read the information from this file and I wll do something with that information 

First ! I will write logic that calulates how many products I have Per Supplier . I will list the company, so all 3 companies with their respective number of products  

Then I will write another logic that lists inventory products that have inventory which is less than 10

Third exercise is going to be to list each company with their respective total inventory value 

Last Exercise I will calculate inventory for each product so product count times price, and I will write that value  to additional column in the spreadsheet and after I will save that updated spreadsheet file programmatically using Python 

#### Install Package 

Now I want to read `inventory.xlsx` file so basically let our Python program read the contents of that file bcs I want to write a logic base on the values that are in this inventory file, I want to calculate stuff 

There is a built-in `module` in Python that allows me to work with files generally not specific for spreadsheet 

<img width="826" alt="Screenshot 2025-04-22 at 11 59 53" src="https://github.com/user-attachments/assets/11d27902-e500-4dca-8dda-97fe5aa4a762" />


Also there is a external package that allow me to work with spreadsheets specificly . Much more function and much easier to use . That Package call `openpyxl`

To install `openpyxl` : `pip install openpyxl` 

!!! NOTE : Wondering why there are some packages with basically a dot inside and some without, these are the packages that we install Python packages, these are the packages that we install, Python Packages and we know that bcs that `__init__.py` file inside and the one without dot, they are just folders with bunch of files inside but they are not Python packages . 

 - And some of those packages I see other packages as well with their own `__init__.py` file so basically hierarchy of multiple packages . and at this point I will say that the word `library` describes package that includes multiple other packages which has a hierarchy of packages

 - So we have `module` which is one python file -> Then I have package which is hierachy of multiple `modules` with `__init__.py` file inside -> Then I have Library which is multiple packages together in a hierachy

#### Implementation 

`openpyxl.load_workbook()` is a function in order to read my spreadsheet file . 

 - This function will load a workbook and all is contents and later I want to do something with that content

First task is to calculate how many products I have per supplier and then list the names of the supplier with that respective number of products 

Second Task is to calculate total inventory value per supplier meaning in my lists for each product I have number of units for the product and the price so basically for each supplier 

Third task is to print out all the products that have inventory less than 10 . 

Fourth task is to add some value inside the spreadsheet

## OOP

For example : An Application with lots of users like LinkedIn . We have user and each user has information (email, name, password, current_job_title). User can change their anything on their profile in order to do that I have to create function 

In the program we need some way to define kind of the blueprint for a user, for all the Data and Function. 

I want to create a blueprint once and I can use the blueprint for all of those Data and function 

Blueprint for a User call `Class` and specific implementation of that blueprint is called `Object`   

<img width="600" alt="Screenshot 2025-04-22 at 14 21 47" src="https://github.com/user-attachments/assets/5aba6ab5-6897-4395-be3e-7a91e42c69de" />

 I will create a `Class` blueprint for a User and the User class blueprint will define what information a User has and what action user can perform in the Application  and object will contain a User 

 The pieces of data also called attributes for that Class

Class is blueprint for specific objects and blueprint cannot actually have specific values . 

In the Blueprint we don't have any specific value we just have Attribute . Acutal value of those Attribute will be then set when we create an Object from the blueprint . However I need a function that will actually take those specific values and assign them to an object which is created from the blueprint and I will create  from the blue print that function called `def __init__(self)`

`__init__(self)` called a constructor. I have a blueprint and we are construncting object from that blueprint, the constructor function will help us construct objects from the Class 

`self` is refer to the Class it's in . Help us access and reference all the attribute and functions within that class  

`def __init__(self, email, name, password, current_job_title):` Those value must be provide to the Constructur whenever I creating a new object 

Then now I have to create function in the Class that any User in application can do, any user can change the password or change their job title and logically when change password happen by user, user provides a new password in order to override the old one . 

So the flow will be -> Object will be created for that specific user so the initial data for that Object will be provided so we will have the user, email, name, password and current job title 
 
After I have Class I can create a User Object 

Now I create `post.py` Class whenever someone post somthing each post will have their own attribute like actual message .... changing, comment, ....

Then I can have `main.py` that I can use those Class file 

In Python almost everythin is an Object

 - For example: Data type like string, Interget, float, list, set, dictionary. And this `int("10")` or str("50") were actually the constructor we called to create string or integer

 - And the constructor of `int` took a string representation of a number and in its init function and constucted an integer out of it

<img width="600" alt="Screenshot 2025-04-22 at 15 02 49" src="https://github.com/user-attachments/assets/905ed8ff-ad15-4365-bb40-756db0d7e15f" />

## Project API Request to GitLab 

To use Python to talk to external Application . 

!!! NOTE : Communication between 2 Applications, in this case Python Application and Gitlab Application usually happens using a HTTP Protocol .

Python Application will send an HTTP request to Gitlab application and from the Gitlab Application it will get an HTTP response for that request 

HTTP is a protocol that these 2 Applications can communicate with over the Internet 

The concept of 1 Application talking to another is baciscally done using API request . 

Remote Application (GitLab) has an API, these are functions that GitLab make available for other applications to call and we will call those functions from out Python application in order to get the List of projects for my user and that communication or Python asking for this information is going to be an API request and what we get in response from this GitLab API is going to be API response 

#### Implementation 

In Python in order to make external request to remote applications we will need a module called `requests`

`requests` package now has functions, variables and objects that we can use to talk to these remote Application like GitLab  

I can also make request to change something 

To make a request : `requests.get("<API-URL>")`

JSON is a standard format that all programming languages understand and usally when 2 applications communicate with each other which are written in different languages and with different technologies with JSON they have common format for communication and this request module basically gives us this JSON function to read the JSON format that GitLab sent us . So JSON function will read the JSON response from GitLab and turn it into one of the Python Data Types   

## Boto Library AWS SDK for Python

AWS pretty complex It has tons of Services and Components, and they are projects that run 100 or 1000 of servers and create 100 or 1000 of resousrces on AWS . As we saw in Terraform module, it's much more efficient to automate the process of creating servers and configuring them, than doing all work manually . So I created Terraform projects that automate creating EC2 instance with all the needed resources like SG, key pair, as well as automated EKS . As well as automated EKS Cluster creation and configuration . 

What about automating repetitive maintenance tasks like backups and cleanups or updating 100 servers by adding new tags to them or doing heath checks and monitoring on these 100 of server or cluster components one of the way doing that by writing Python program 

Python has a library called `Boto` that makes it possible to work with AWS `resources` .

 - I can create resources, configure resources fetch the data about them and do all sorts operations on  my AWS account

!!! NOTE : Even though Terraform and python can both do some of the same things of of IaC provisioning it is importnant to know which tool to use for which specific tasks, and . 

#### Instal Boto and connect to AWS 

To install Boto3: `pip install boto3`

Just like we did with Terraform I want to connect to AWS account and authenticate with our AWS User .

We can configure using AWS configure command if I have aws CLI installed locally, which sets four values (aws_access_id, aws_access_secret_key, region, output format)

`Boto3` will automatically take these credentiasl and the default region information to connect to AWS and authenticate with it . That mean I do not need to do anything 

My AWS credentials live here : `ls ~/.aws`

#### Try out Boto3 

I will create AWS client from Boto Library, I will list all the VPCs available in the region that is configured in the default region configured for AWS 

!!! Important : `Boto3` library can do pretty much anything in AWS account, much more than Terraform could do . So whenever I am writing logic to do something in AWS, create resources, configure resoruces, maybe automate some maintainance task, I would need to use the documentation as a reference, bcs there is no way that I can remember all the function names and all the parameters that I need to use . 

 - Also the purpose of this part is teach me how to work with documentation to be able thendo anything that I can acutally want to do for my own project

All the Services have their own functions, own set of functions that I can work with 

Basically in `Boto3` I have a `Client` for EC2 that will be able to connect to AWS and do something for EC2 related components . And that is why we gonna create a Client from EC2 : `client = boto3.client('ec2')`

 I will get into `describe_vpcs`, then I will jump to the description of that function . 

 - First I need to know a function name . To call function `client.describe_vpcs()`

 - What Parameter does it take. What do I need to pass in to get a result . I will have the list of Parameter and the describtion of what the Parameter actually are as well as which data types I should use for those parameters

 - Also for each parameters I see whether that parameter is required or not . So basically whether I alway have to set them when I call this function or I can leave that out .
 
 - Also we need to know what are we getting as a result of  the function call in `Response Syntax` . The reason why we need to know how the response looks like is so that we can actually get the specific values from that response, the values that we are interested in

 - It's important to get used to and comfortable with reading values from the nested response object

We must write program so it works whether we have 1 elements or 100 or even no element at all in the list 

```
import boto3

ec2_client = boto3.client('ec2')

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
```

#### Connect to non-default region 

What if I want to get infomation from another Region, but I don't want to change the default Region in `~/aws/config`

So in `ec2_client = boto3.client('ec2')` I can pass in the region name `ec2_client = boto3.client('ec2'), region_name="eu-west-3"` . This way I can override the default region .

Instead of directly put value in parameter I pass value via key=value like this `region_name="eu-west-3` this is called name parameter

When I have a function that accepts 10 optionals parameters, But I only want to provide 2 of the parameter values, most of them are optionals . In that case Python need to know for which parameters I am providing these values, So we have to tell that explicitly by using named parameter  . With name parameters I can tell exactly which value I am setting for which parameters

#### Create VPC and Subnet 

In docs -> Go to EC2 -> Go to Service Resources 

What is the difference between `resource` and `client` ? 

 - `Client` is more low-level API, It mean I need to explicitly specify exactly which resource I want to connect to for every single function that I execute

 - `Resources` is basically like a wrapper around client that makes a little bit high level, a little bit more easier to work with different resources

This will return `VPC resource` . Give a resource Object back so we can use it for subsequent call 

```
vpc = ec2_resource.create_vpc(
  CidrBlock = "10.0.0.0/16"
)

# Now I have vpc Object I can create a subnet on that vpc Object

vpc.create_subnet()
```

If we were using `Client` instead, I would have to specify the VPC ID and the subnet 

```
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
```

## Terraform vs Python When to use which tool

Terraform is much better tools for Create, Delete and Manage IaC . More High level and easier to write 

#### Use Case for Boto3 

I can do thing that I wouldn't be able to do with Terraform 

I can do more complex logic like conditionals and decide when to do what compared to Terraform 

Boto is a full-fledged AWS library so it allow me to do much more and get more information also about the `resources` from AWS compared to Terraform AWS provider 

For example I can do Monitoring IaC, doing backups, doing cleanups, doing tasks that are scheduled basically that run every pre-configured time, which all these thing I can acutally can't really do in Terraform . 

I can add Web Interface to my Python project and execute all these backup and cleanup task manually, maybe just add some buttons, or do a cleanup or maybe display the health 

## Health Check EC2 Status Check

Let's say we have 100 Servers on AWS using Terraform and have some Auto Scaling Configured . All the time new Instances get created, some get deleted, etc. And Since EC2 Instances always need some tome to fully initialize I acutally want to know which instances are in which State, So that I have a good overview of which Instances are running which ones are in ready State, or which one are currently initialzing, etc 

So bassically I want to get Status check from EC2 Instances using Python's Boto library 

#### Preparation : Create EC2 Instances with TF .

I will use the Terraform Project in Teraform Module to create 3 EC2 Instances in `Create-3-EC2-Instance-for-Health-Check-Python` branch (https://github.com/ManhTrinhNguyen/Infrastructure-as-code-Terraform)

To get 3 Instances instead of one I just need to copy `resource aws_instance` 3 times and change the name

Now I have 3 Instances in my AWS . I can use Python `Boto3` to list or fetch the data on all EC2 Instances running in this region . 

To get all the EC2 instances from Specific region in the VPC they are running :

```
import boto3

ec2_client = boto3.client('ec2')

ec2_resource = boto3.resource('ec2')

# To get all the Reservations

reservations = ec2_client.describe_instances()

# Loop through the Reservations to get Reservation
for reservation in reservations["Reservations"]:
# Get Instances
instances = reservation['Instances']

# Loop through the instances to get instance
for instance in instances:
    # Get Instance ID 
    instance_id = (instance["InstanceId"])
    
    # Get Instance Name 
    instance_name = (instance["State"]["Name"])
    
    print(f"Status of Instance {instance_id} is              {instance_name}")
```

 - `Reservations` basically represents starting or launching multiple instances . One `reservation` is an act or intention of launching or starting Instances, so we might have multiple `reservations` and then each reservation can have multiple Instances .

#### Print EC2 Status Check 

I need to check 2 things in Instances .

 - It take some time to initialzie

 - When it ready to use

To check EC2 Status I call function `describe_instance_status`

```
import boto3

ec2_client = boto3.client('ec2')

statues = ec2_client.describe_instance_status()

for status in statues['InstanceStatuses']:
  instance_status = (status["InstanceStatus"]["Status"])
  system_status = (status["SystemStatus"]["Status"])
  instance_id = status["InstanceId"]
  print(f"Instance {instance_id} status is {instance_status}, system status is {system_status}")
```

## Scheduling the Status Checks 

Obviously Status will changes . Just executing the program once doesn't make sense . If we are monitoring and basically want to have an overview of live updates of instance statuses, we can't just be sitting there and executing this program manually

So I want some kind of sheduler, some automate process, that runs trigger the program basically every hour or every 10 mins or maybe every single day at 1am  

So I will write a scheduler, that will execute this specific logic every 5 mins 

 - First Add Schelue Library called `schedule` : `pip install schedule`

```
import boto3
import schedule

ec2_client = boto3.client('ec2')

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
```

## Configure Server Add Environment Tags to EC2 

Let's say we have 20 Servers in us-west region which are used as production servers but we also have 10 servers in us-north region . Basically we created all these Servers using Terraform in both of these Regions and now we want to add tags to all these servers, we want to add environment dev and environment prod servers to respective instances 

With Python logic I will basically get the instances for each region and add the correct tag to all the Servers in that region 

Collect all the ID then execute 1 Function create tags with all the Instances ID Instead of executing the create tags function multiple times  

Making 1 request to 100 servers much more efficent than making 100 requests to 100 servers 

When we write a program in addition to program just working as expected obviously it should also work effciently 

```
import boto3

# Get EC2 Client from us-west-1
ec2_client_us_west_1 = boto3.client('ec2', region_name="us-west-1")

# Get EC2 Resource from us-west-1
ec2_resource_us_west_1 = boto3.resource('ec2', region_name="us-west-1")

reservations_us_west_1 = ec2_client_us_west_1.describe_instances()["Reservations"]

# Create Instance_ID list 
instance_ids_us_west_1 = []

# Iterate through the Reservations 
for reservation in reservations_us_west_1:
  instances = reservation['Instances']
  for instance in instances:
    # Get ID of Instance
    instance_id = instance["InstanceId"]
    instance_ids_us_west_1.append(instance_id)
    

response = ec2_resource_us_west_1.create_tags(
    Resources=instance_ids_us_west_1,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)
```

For another region I just need to do the same logic as the logic above with different region name

## Print EKS Cluster Info

Let's say I have created 10 EKS Cluster in my AWS account, using Terraform . And  I want to have an overview of all my running clusters, I want to see which status they have, are they in active state, are they in failed or creating or whatever state they have . We want to print that out as well as we want to know for each cluster which Kubernetes version the cluster is running and also a Cluster Endpoint  

What I want is to get all the clusters in that region and then go through the Cluster value itself and basically check the status of the Cluster  

To get all the Clusters Name : `clusters = client.list_clusters()['clusters']` . This will be a list of Cluster name 

To get detail infomation for specific Clusters : `response client.describe_cluster(name= <name-of-cluster>)` . 

 - From that I can get cluster status : `cluster_status = response['cluster']['status']`

 - Also I can get Cluster endpoint : `cluster_endpoint = response['cluster']['endpoint']`

This is something that I want to run multiple time . Bcs the Status basically may change the endpoint and version will most probaly stay the same most of the time unless there is a new version 

## Automate backup for EC2 Instances 

I will create Python program that automates backups for EC2 Instances . 

I will create snapshots of volumes for our EC2 Instances 

Volumes are AWS Storage components that basically stores the data of the EC2 instance and every EC2 Instance has its own volume where it writes all of its data 

Think of Volume as a hard drive for my EC2 Server . Every Server needs a hard drive to save the data . So when we create EC2 instance a volume get created automatically and get attached to that EC2 Instance and when we delete EC2 Instances volume get deleted as well 

Volume Snapshot is a copy of a volume what inside the volume or that hard drive basically, exactly at that time when we create a snapshot  

And snapshot are very important for data backups and for creating new volumes 

I want to automate this Snapshot if I have 100 of Instances to ensure that I always have latest backup data available incase EC2 Instance dies or volumes get deleted or maybe data gets corrupted in that volume 

Let's say I have 50 EC2 Volumes that have not been backed up, but recently some of the EC2 Instances crashed and we lost the volumes and data so I will create backup for it  

I will create Python program that will create snapshots automatically every day at a specificed time 

I will write a schedule task that go through the volumes everydays and then creates snapshots or backups, volume backups from those volumes 

To get a list a volume I will go to EC2 Client -> `volumes = ec2_client.describe_volumes()['Volumes']` . In order to create Snapshot we need volume ID . 

```
for volume in volumes:
  print(volume['VolumeId'])
```

To create Snapshot :

```
for volume in volumes:
  volume_id = (volume['VolumeId'])

  new_snapshot = ec2_client.create_snapshot(
    VolumeId=volume_id
  )

  print(new_snapshot)
```

I will have a task that regularly executes and does a backup every single day or maybe every one hour depending on how sensitive my data is, how risky it is or how dangerouse it would be to basically lose the data . So a need a Scheduler 

```
import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-west-1")

volumes = ec2_client.describe_volumes()['Volumes']

def volume_backup():

  for volume in volumes:
    volume_id = (volume['VolumeId'])

    new_snapshot = ec2_client.create_snapshot(
      VolumeId=volume_id
    )

    print(new_snapshot)


# Scheduler everydays at 1pm
schedule.every().day.at("13:00").do(volume_backup)

# To run the Scheduler I have to execute that 
while True:
  schedule.run_pending()
```

What If I want to only create a snapshot for only Production server ? 

In `describe_volume` I can possible filter the result .

I can assign my volumes specific tags and then I can filter the volumes using that tag . 

If I have maybe 100 servers I would not do that manually . 
In this case I would either get all the Instances using their tags and then basically set instance ID and filter volumes for those instance IDs . 

Or I would just write a Python program that adds tags to all the volumes that are attached to production servers 

I will get Volume with a `tag: prod` like this then I will create snapshot from it 

```
volumes = ec2_client.describe_volumes(
  Filters=[
    {
      'Name': 'tag:environment',
      'Values': [
        'production'
      ]
    }
  ]
)['Volumes']
```

## Automate cleanup of old Snapshot

In addition to creating these automated backup snapshots, I want to write a program that will clean up old snapshots from AWS account, since I am not need those old snapshots . I can scheduler to cleanup, maybe we want to clean up the old snapshots every week 

In order to cleanup the Snapshots, I basially have to get all the Snapshots from our AWS account . So basically I want to be able to list all the snapshot that I have created in our region in AWS account . And once we have the list of all those snapshots in our Python program, we want to go through them and check the creation date and I want to find the latest 2 and delete the rest 

To get a list of all snapshot : `describe_snapshots()` . This snapshot function are atucally return snapshot that AWS also does automatically . These are Snapshot that created for EC2 Instance volumes but there are another snapshots that AWS also creates in the background 

To sort a list by a value of a dictionary, I will use the `sorted()` built-in function that Python gives me.  
It takes a `list` and a `key=` parameter to tell how I want to sort.  
In this case, I want to sort these snapshots using `snapshot['StartTime']`.

To delete a Snapshot in AWS, I use:

```
ec2_client.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
```

---

I create an EC2 client where I have my Snapshots:

```
ec2_client = boto3.client('ec2', region_name="us-west-1")
```

Then I fetch all the Snapshots that I have created, by specifying `OwnerIds=['self']`:

```
snapshots = ec2_client.describe_snapshots(
  OwnerIds=['self']
)['Snapshots']
```

At this point, I have an unsorted list of snapshots.

I want to sort them by `StartTime`, so the most recent snapshots appear first.  
I use `sorted()` function together with `itemgetter('StartTime')`:

```
from operator import itemgetter

sort_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)
```

Now I have the list sorted in **descending order**.

---

Instead of iterating through the whole list, I want to **skip the first 2 elements** (the most recent snapshots) and delete the rest:

```
def cleanup_snapshot():
  for snapshot in sort_by_date[2:]:  # Skip the latest 2
    print(snapshot['StartTime'])
    print(snapshot['SnapshotId'])

    # Delete snapshot
    response = ec2_client.delete_snapshot(
      SnapshotId=snapshot['SnapshotId']
    )

    print(response)
```

---

I use the `schedule` library to schedule the `cleanup_snapshot()` function to run **every day at 1PM**:

```
import schedule

schedule.every().day.at("13:00").do(cleanup_snapshot)
```

To actually make the scheduler run, I have to use an infinite loop:

```
while True:
  schedule.run_pending()
```

---

#### Full Code

```
import boto3 
from operator import itemgetter
import schedule

# Create EC2 client
ec2_client = boto3.client('ec2', region_name="us-west-1")

# Fetch snapshots owned by self
snapshots = ec2_client.describe_snapshots(
  OwnerIds=['self']
)['Snapshots']

# Sort snapshots by StartTime descending
sort_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)

# Cleanup function
def cleanup_snapshot():
  for snapshot in sort_by_date[2:]:  # Skip first 2 snapshots
    print(snapshot['StartTime'])
    print(snapshot['SnapshotId'])

    response = ec2_client.delete_snapshot(
      SnapshotId=snapshot['SnapshotId']
    )

    print(response)

# Schedule the cleanup everyday at 1 PM
schedule.every().day.at("13:00").do(cleanup_snapshot)

# Keep the scheduler running
while True:
  schedule.run_pending()
```


## Automate cleanup of old Snapshot multiple Volumes

If I have multiple volumes and creating snapshots for many different volumes then I can't just list all the Snapshot and then remove everything other than the most recent two . Bcs I have to actually differentiate which Snapshot belong to the same Volume so we have to do that logic, basically, for a Snapshots of each and every volume 

In the `describe_snapshots()` I will add additional parameter called `volumeId` so I will listing this Snapshot of one specific volume at a time, and then that will give me a list of snapshots per volume, then I can do sorting and removing everything 

To get volume ID I have to list all the volumes that I have, the one that I have created Snapshot on, so in order to do that, I am going to the Volume backup program that I created and this is basically the logic that created those snapshots from volumes that have name `tags` with value `prod`

In this script, I connect to EC2 and filter **volumes** based on a **tag key**.

I want to find **all volumes** that have a tag `environment=dev`, then **fetch their snapshots**, **keep the two latest snapshots** for each volume, and **delete the older ones**.

---

First, I create an EC2 client:

```
ec2_client = boto3.client('ec2', region_name="us-west-1")
```

---

Then I fetch volumes that match a certain tag.  
In this case, I want volumes that have the tag:

- Key: `environment`
- Value: `dev`

```
volumes = ec2_client.describe_volumes(
  Filters=[
    {
      'Name': 'tag:environment',
      'Values': ['dev']
    }
  ]
)['Volumes']
```

---

For each volume, I get the `VolumeId` and find all snapshots that were created from that volume:

```
for volume in volumes:
  volume_id = (volume['VolumeId'])

  snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
      {
        'Name': 'volume-id',
        'Values': [volume_id]
      }
    ]
  )['Snapshots']
```

---

I then sort the snapshots by their `StartTime` in descending order, so the newest ones come first:

```
sort_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)
```

---

Now, I skip the first 2 newest snapshots and delete the older ones:

```
for snapshot in sort_by_date[2:]:
  print(snapshot['StartTime'])
  print(snapshot['SnapshotId'])

  response = ec2_client.delete_snapshot(
    SnapshotId=snapshot['SnapshotId']
  )

  print(response)
```

---

#### Full Code

```
import boto3
from operator import itemgetter

# Create EC2 client
ec2_client = boto3.client('ec2', region_name="us-west-1")

# Fetch volumes with specific tag
volumes = ec2_client.describe_volumes(
  Filters=[
    {
      'Name': 'tag:environment',
      'Values': ['dev']
    }
  ]
)['Volumes']

# Loop through volumes
for volume in volumes:
  volume_id = (volume['VolumeId'])

  # Fetch snapshots for the volume
  snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
      {
        'Name': 'volume-id',
        'Values': [volume_id]
      }
    ]
  )['Snapshots']

  # Sort snapshots by StartTime descending
  sort_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)

  # Delete snapshots, keep 2 latest
  for snapshot in sort_by_date[2:]:
    print(snapshot['StartTime'])
    print(snapshot['SnapshotId'])

    response = ec2_client.delete_snapshot(
      SnapshotId=snapshot['SnapshotId']
    )

    print(response)
```

---

#### Notes

- Only volumes with the tag `environment=dev` will be checked.
- Only snapshots related to each volume are considered.
- Always keep the 2 most recent snapshots for safety.
- Be careful: deleting snapshots is **permanent** and cannot be undone.

## Automate restoring EC2 Volume from the Backup 

Now I have the Snapshot ? How acutally I can use that Snapshot . Let's say I have an Instance running and the volume data on  that Instance gets corrupted, I want to recover the latest working state of that EC2 Instance by creating a new volume from a snapshot, then attaching that volume to the EC2 Instance so that it can continue running 

This Python script automates the process of restoring an EBS volume from the most recent snapshot associated with a specific EC2 instance. It uses the AWS SDK `boto3` to:

1. Identify the volume attached to an EC2 instance.
2. Retrieve the latest snapshot of that volume.
3. Create a new EBS volume from the snapshot.
4. Wait until the volume becomes available.
5. Attach the new volume to the EC2 instance.

#### Prerequisites

AWS account with EC2 and EBS permissions.
AWS credentials configured (`~/.aws/credentials` or via environment).
`boto3` installed: `pip install boto3`

```
import boto3 
from operator import itemgetter

# Create EC2 client and resource in a specific AWS region
ec2_client = boto3.client('ec2', region_name='us-west-1')
ec2_resource = boto3.resource('ec2', region_name='us-west-1')

# ID of the EC2 instance whose volume will be restored
instance_id = "i-0c7270f4c6bb9b931"

# Step 1: Get the volume attached to the given EC2 instance
volumes = ec2_client.describe_volumes(
  Filters = [
    {
      'Name': 'attachment.instance-id',
      'Values': [instance_id]
    }
  ]
)

# Pick the first (or only) volume from the response
instance_volume = volumes['Volumes'][0]

# Step 2: Get snapshots that belong to you and are associated with the volume
snapshots = ec2_client.describe_snapshots(
  OwnerIds=['self'],  # Limits results to snapshots you created
  Filters=[
    {
      'Name': 'volume-id',
      'Values': [instance_volume['VolumeId']]
    }
  ]
)['Snapshots']

# Sort snapshots by StartTime descending (latest first) and pick the newest one
latest_snapshot = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)[0]

# Step 3: Create a new EBS volume from the latest snapshot
new_volume = ec2_client.create_volume(
  SnapshotId=latest_snapshot['SnapshotId'],
  AvailabilityZone="us-west-1a",  # Must match the AZ of the instance
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

# Step 4: Wait for the volume to become 'available' before attaching
# This is important to avoid attachment failure due to timing
while True:
  volume = ec2_resource.Volume(new_volume['VolumeId'])
  print(volume.state)  # Print status: creating, available, etc.
  if volume.state == 'available':
    # Attach the new volume to the EC2 instance at a specified device path
    ec2_resource.Instance(instance_id).attach_volume(
      VolumeId=new_volume['VolumeId'],
      Device='/dev/xvdb'  # Must differ from existing device like /dev/xvda
    )
    break
```

#### NOTE

Make sure the AvailabilityZone used in create_volume() matches the AZ of your EC2 instance.

Avoid reusing existing device names (/dev/xvda, /dev/xvdb, etc.).

Ensure IAM permissions include ec2:Describe*, ec2:CreateVolume, and ec2:AttachVolume.

## Hanlding Error

When doing automated tasks things can go wrong . Maybe Snapshot creation didn't work or Volume attachment didn't work etc .... At any of the codes something could go wrong 

It is very important to write a code which is able not just execute request and function, but also handle erros when they occur, this is so important when I execute some critical operation . If `Error` not handle in the correct ways it could lead to data loss or server downtime etc.. . Insteade I catch the Error correctly and handle them, as well as print them out so we know what exactly happended during the program execution that can help me with debugging 

Critical to think is if I am creating components or even more importantly, changing or updating existing resource and things go wrong there, it half work then I might end up with a weird state, we might actually break thing if I don't handle these erro properly 

For example :  If creation Snapshot goes wrong so it kinda work but not really or basically I end up with a bad Snapshot like not usable Snapshot, then handling of that error should be to delete that snapshot instead of just keep it in the list, bcs then there is a risk that we might restore volume from that bad snapshot .

Another Example : If we are updating something in the server, and just some of the tasks work, but some of the task works but some of them fail we should actually be able to handle that error, and kind of `roll back` the change that we did 

When I am working with Terraform, it will take care of this kind of stuff, bcs it has the state managment in place, so it can handle this kind of situations . In Python however I have to do everything myself 

To do that I will use `try-except` . I can catch the error when they occur and then do something when it happen 

```
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

```

## Website Mornitoring

#### Preparation Steps 

I will use Linode as a Cloud Server 

Once Server installed, I will create Docker and I will rung simple Nginx container on it 

Once I have Nginx Container up and running . I will write python program that checks the application  endpoint and check status of that applications

Bassically It just make an HTTP request to it and checks that we have a successful reply from the application and if the response from the application is not successful, either application has some problems or application isn't accessible at all, maybe server is down, maybe the container just crashed . If that happen my Python program will basically alert us or notify through email that website is down and we need to do something with it 

That mean I will configure Python program to send email to my email address 

As a next step, I will automate fixing the problem as well .

Once we get notified per email, we will then extend the Python Logic to restart the Docker container on the server or if the server is not accessible restart the server and then Docker container on it 

#### Create Server and run Nginx container 

Go to Linode -> Create Virtual Machine Linode -> Choose distribution Debian 11 -> Region -> 2 GB server -> rootpassword -> Create SSH key -> Create Server 

SSH to a Server : `ssh root@<ip-address>`

To install Docker, depend on the instruction that we are on we can follow the instruction in Docker Document 

To install Docker for Debian : 












