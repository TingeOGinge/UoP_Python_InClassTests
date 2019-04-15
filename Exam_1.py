def biscuitSlices():
    trayLength = float(input("What is the length of your tray in cm? "))
    trayWidth = float(input("What is the width of your tray in cm? "))
    numOfSlices = int((input("How many slices should the mixture be cut into? ")))
    
    biscuitThickness = trayLength / numOfSlices
    biscuitArea = biscuitThickness * trayWidth
    biscuitChocCals = 900 / numOfSlices
    biscuitTotalCals = (biscuitArea * 2) + biscuitChocCals
    brotherBiscuits = 1000 // biscuitTotalCals
    
    print("The thickness of each biscuit =", biscuitThickness, "cm")
    print("The area of each biscuit =", biscuitArea, "cm^2")
    print("The number of calories per biscuit (inc chocolate topping) =", biscuitTotalCals)
    print("The number of biscuits the brother can eat =", int(brotherBiscuits))
    
biscuitSlices()