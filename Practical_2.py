import math

#Function designed to evaluate the slope and distance between two points
def warmUpExercises():
    x1 = 1
    y1 = 2
    x2 = 4
    y2 = 6
    
    slope = (y2 - y1) / (x2 - x1)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    print("Slope =", slope, "Distance =", distance )
    
    #radius = math.sqrt((headOuter.getX() - headInner.getX())**2 + (headOuter.getY() = headInner.getY())**2)


#Asks the user to enter the radius of a circle and evaluates the circumference 
def circumferenceOfCircle():
    radius = float(input("Enter the radius of your circle "))
    circumference = 2*math.pi*radius
    print("The circumference of your circle is", circumference)


#Asks the user to enter the radius of a circle and evaluates the area
def areaOfCircle():
    radius = float(input("Enter the radius of your circle "))
    area = math.pi*radius**2
    print("The area of your circle is", area)
    
    
#Asks the user for the diameter of the pizza, evaluates the area of the pizza, then the cost of the pizza based on the cost being 1.5 pence per cm^2
def costOfPizza():
    diameter = eval(input("What is the diameter of your pizza? "))
    area = math.pi*(diameter / 2)**2
    cost = area * 1.5
    print("The cost of your pizza is", cost, "pence")
    
    
#Asks the user for 4 numbers that make up two coordinates then calculates the slope of the connecting line
def slopeOfLine():
    x1 = int(input("Enter the value for x1 "))
    y1 = int(input("Enter the value for y1 "))  
    x2 = int(input("Enter the value for x2 "))  
    y2 = int(input("Enter the value for y2 ")) 
    
    slope = (y2 - y1) / (x2 - x1)
    print("The slope of your line is equal to", slope)
    
    
#USer inputs 4 values to represent two points, the function then evaluates the distance
def distanceBetweenPoints():
    x1 = int(input("Enter the value for x1 "))
    y1 = int(input("Enter the value for y1 "))  
    x2 = int(input("Enter the value for x2 "))  
    y2 = int(input("Enter the value for y2 ")) 
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    print("The distance between your two points is", distance)


#User inputs speed in km/hr and duration in hours, the function evaluates the distance travelled and fuel consumed, assuming 5 km/litre
def travelStatistics():
    avgSpeed = float(input("What is your average speed in km/hour? "))
    duration = float(input("What is the duration of your trip in hours? "))
    distanceTravelled = avgSpeed * duration
    fuelUsed = distanceTravelled / 5 
    
    print("Overall you have travelled", distanceTravelled, "km and used approximately", fuelUsed, "litres of fuel")


#Outputs the sum of the first n positive integers where n is provided by the user
def sumOfNumbers():
    n = int(input("Please enter a whole number "))
    result = 0
    
    for i in range(n):
        result += i+1

    print("The sum of the first n positive integers, where n =", n, "is equal to", result)


#User input how many numbers they'd like to average, then inputs the numbers. Function evaluates the average and prints    
def averageOfNumbers():
    numCount = int(input("How many numbers would you like to input "))
    total = 0
    
    for i in range(numCount):
        n = eval(input("Input a number "))
        total += n
    
    totalAverage = total / numCount
    print("The average of your numbers =", totalAverage)
    

#First attempt at a program that breaks down a value of pennies into the different denominations - Highly inefficient 'parser' compared to the second attempt below that uses lists and a loop
def selectCoins1():
    moneyRemaining = int(input("How much pennies do you have? "))
    twoPound = 0
    onePound = 0
    fiftyPence = 0
    twentyPence = 0
    tenPence = 0
    fivePence = 0
    twoPence = 0
    onePence = 0
    
    if (moneyRemaining / 200 >= 1):
        twoPound = moneyRemaining // 200
        moneyRemaining %= 200
    
    if (moneyRemaining / 100 >= 1):
        onePound = moneyRemaining // 100
        moneyRemaining %= 100
    
    if (moneyRemaining / 50 >= 1):
        fiftyPence = moneyRemaining // 50
        moneyRemaining %= 50
    
    if (moneyRemaining / 20 >= 1):
        twentyPence = moneyRemaining // 20
        moneyRemaining %= 20
    
    if (moneyRemaining / 10 >= 1):
        tenPence = moneyRemaining // 10
        moneyRemaining %= 10
    
    if (moneyRemaining / 5 >= 1):
        fivePence = moneyRemaining // 5
        moneyRemaining %= 5
    
    if (moneyRemaining / 2 >= 1):
        twoPence = moneyRemaining // 2
        moneyRemaining %= 2
    
    onePence = moneyRemaining
    
    print("That is equal to", twoPound, "x £2,", onePound, "x £1,", fiftyPence, "x 50p,", twentyPence, "x 20p,", tenPence, "x 10p,", fivePence, "x 5p,", twoPence, "x 2p,", onePence, "x 1p")


#Second attempt at evaluating the denominations of n pence into larger denominations, much more efficient than the first attempt 
def selectCoins2():
    money = int(input("How many pennies do you have? "))
    amounts = [0,0,0,0,0,0,0,0]
    denominations = ["£2","£1","50p","20p","10p","5p","2p","1p"]
    amountsInPence = [200,100,50,20,10,5,2,1]
    for i in range(8):
        if money >= amountsInPence[i]:
            amounts[i] = money // amountsInPence[i]
            money %= amountsInPence[i]
            print(denominations[i], "x", amounts[i])


#Taking the algorithim from selectCoins2() I have expanded it to accept 50, 20, 10 and 5 pound notes 
def selectCoins3():
    money = int(input("How many pennies do you have? "))
    amounts = [0,0,0,0,0,0,0,0,0,0,0,0]
    denominations = ["£50","£20","£10","£5","£2","£1","50p","20p","10p","5p","2p","1p"]
    amountsInPence = [200,100,50,20,10,5,2,1]
    for i in range(12):
        if money >= amountsInPence[i]:
            amounts[i] = money // amountsInPence[i]
            money %= amountsInPence[i]
            print(denominations[i], "x", amounts[i])


#--------------------------------------------------------------------

def piFromUser():
    n = int(input("How many terms would you like to sum to reach your pi approximation? "))
    piApprox = 4/1
    switch = True
    
    for i in range(3, n*2+1, 2):
        if (switch == True):
                piApprox -= 4 / i
                switch = False 
        
        else:
            piApprox += 4 / i
            switch = True
    
    print("Your approximation of pi =", piApprox)
    print("You are", math.pi - piApprox, "away from actual pi")
    
def fibonacciSequence():
    n = int(input("What number in the fibonacci would you like to see? "))
    fibonacci = [1, 1]
    
    for i in range (1, n+1):
        fibonacci.append(fibonacci[i] + fibonacci[i-1])
    
    print(fibonacci[:n])
    

    
def newtonsSqrt():
    x = int(input("What number would you like the square root of? "))
    n = int(input("How many guesses do I get? "))
    guess = x / 2
    
    for i in range(n):
        if (guess**2 != x):
            guess = (guess + x / guess) / 2
    
    print("After making", n, "guesses, I have come up with the answer", guess)
    print("This is", math.sqrt(x) - guess, "away from the correct answer")

newtonsSqrt()    
    
    
    




