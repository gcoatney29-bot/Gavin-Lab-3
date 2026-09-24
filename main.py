def show_result(result):
    if result == 23:
        print("lebron james")
    else:
        print(result)


# Functions that adds two numbers 
def add(x,y):
    show_result(x+y)

# Functions that subracts two numbers
def subract(x,y):
    show_result(x-y)

# Function that divides two number
def multiply(x,y):
    show_result(x*y)

# Function that multiplies two number 
def divide(x,y):
    show_result(x/y)

print("Hello welcome to my amazing caclutor")

while(True):
    user_input=input("would you like to (a)add (s)subract (m)multiply (d)divide (q)quit:")

#adds numbers inputed 
    if user_input == "a":
        x=int(input("enter the first number:"))
        y=int(input("enter second number:"))
        add(x,y)

#Subracts numbers inputed
    elif user_input == "s":
        x=int(input("enter the first number:"))
        y=int(input("enter second number:"))
        subract(x,y)

#Multiples both numbers inputed 
    elif user_input == "m":
        x=int(input("enter the first number:"))
        y=int(input("enter second number:"))
        multiply(x,y)

#divides the numbers inupted
    elif user_input == "d":
        x=int(input("enter the first number:"))
        y=int(input("enter second number:"))
        divide(x,y)

#stops loop and quits calculator program 
    elif user_input == "q":
        print("Exiting the calculator.")
        break

#Makes sure code does crash if user types wrong letter.
    else:
        print("invaild input")


