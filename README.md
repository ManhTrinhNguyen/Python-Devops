[Automation](#Automation)

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

## Automation with Python (Spreadsheet)

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

## Project: API Request to GitLab 

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

## Boto Library (AWS SDK for Python)

AWS pretty complex It has tons of Services and Components, and they are projects that run 100 or 1000 of servers and create 100 or 1000 of resousrces on AWS . As we saw in Terraform module, it's much more efficient to automate the process of creating servers and configuring them, than doing all work manually . So I created Terraform projects that automate creating EC2 instance with all the needed resources like SG, key pair, as well as automated EKS . As well as automated EKS Cluster creation and configuration . 

What about automating repetitive maintenance tasks like backups and cleanups or updating 100 servers by adding new tags to them or doing heath checks and monitoring on these 100 of server or cluster components one of the way doing that by writing Python program 

Python has a library called `Boto` that makes it possible to work with AWS `resources` .

 - I can create resources, configure resources fetch the data about them and do all sorts operations on  my AWS account

!!! NOTE : Even though Terraform and python can both do some of the same things of of IaC provisioning it is importnant to know which tool to use for which specific tasks, and . 



