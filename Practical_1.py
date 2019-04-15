# Practical Worksheet 1: Getting started with Python
# A kilgroams to pounds conversion program
# Dillon O'Shea, up887062
# September 2018

#Displays "Hello, world" on the screen
def sayHello():
    print("Hello, world")

#Displays integers from 1 - 10
def count():
    for i in range(10):
        print(i+1)

#Converts kilograms into pounds and prints the result
def kilos2pounds():
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("The weight in pounds is", pounds)

#Prints my name
def sayName():
    print("Dillon O'Shea")
  
#Prints "Hello" on one line and "World" on another 
def sayHello2():
    print("Hello")
    print("World")

#Converts Euros to Pounds and prints the result    
def euros2pounds():
    euros = float(input("How many euros would you like to convert? "))
    pounds = euros / 1.12
    print(euros, "in pounds is: ", pounds)

#Takes two inputs from the user and displays the sum    
def addUp():
    var1, var2 = input("Input your two numbers like so '1 1': ").split(" ")
    print("The sum of", var1, "and", var2, "equals", float(var1)+float(var2))

#Asks the user how many 1p, 2p and 5p coins they have and prints the sum     
def changeCounter():
    onePence = int(input("How many 1p coins do you have?: "))
    twoPence = int(input("How many 2p coins do you have?: "))
    fivePence = int(input("How many 5p coins do you have?: "))
    print("In total you have", onePence+twoPence*2+fivePence*5, "pennies")

#Prints "hello, world" ten times on separate lines    
def tenHellos():
    for i in range(10):
        print("hello, world")

#Displays a table that shows kilos from 0, 10, 20... 100 and the corresponding values in pounds
def weightsTable():
    print("Kilos \t Pounds")
    for i in range(0, 101, 10):
        kilograms = i
        pounds = 2.2 * kilograms
        print(kilograms, "\t = \t", pounds)

#Calculates 5.5% compound interest on an amount the user enters for n years that the user also enters 
def futureValue():
    investmentOriginal = float(input("How much are you looking to invest? "))
    investment = investmentOriginal
    years = int(input("How long will you keep your investment? "))
    
    for i in range(years):
        investment *= 1.055
    
    print("In", years, "years your investment of", investmentOriginal, "has become", investment)
    print("That is an increase of", investment-investmentOriginal)
