# Functions that adds two numbers 
def add(x,y):
    print(x+y)

# Functions that subracts two numbers
def subract(x,y):
    print(x-y)

# Function that divides two number
def multiply(x,y):
    print(x*y)

# Function that multiplies two number 
def divide(x,y):
    print(x/y)
while(True):
    user_input=input("would you like to (a)add (s)subract (m)multiply (d)divide (q)quit:")
    if user_input == "a":
    # Ask user for their frist and second number
        x=int(input("enter the first number:"))
        y=int(input("enter second number:"))
        add(x,y)
    elif user_input == "s":
        x=int(input("enter the first number:"))
        y=int(input("enter second number:"))
        subract(x,y)
    elif user_input == "m":
        x=int(input("enter the first number:"))
        y=int(input("enter second number:"))
        multiply(x,y)
    elif user_input == "d":
        x=int(input("enter the first number:"))
        y=int(input("enter second number:"))
        divide(x,y)
    elif user_input == "q":
        break



