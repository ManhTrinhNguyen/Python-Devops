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



    
    
