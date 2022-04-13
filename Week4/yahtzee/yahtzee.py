import random
diceList = []
Yahtzee = False

# Create a class for a die (single dice)
# Define any necessary attributes.  Your die class should be able to handle any number of sides such as 4, 6, 8, 10, 12, 20, 100, etc.
# Create the following methods for the class:
# __init__ - Constructor method
class Die:
    def __init__(self, sides, faceNum):
        self.sides = sides
        self.faceNum = faceNum
    
# roll - Roll the die to get a new random value based on the number of sides of the die
    def roll(self):
        self.getCurrentFaceValue(random.randint(1, self.sides))

# getCurrentFaceValue - Get the value currently showing on the die face
    def getCurrentFaceValue(self, newRoll):
        self.faceNum = newRoll

# showDieFace - Display the value currently showing on the die.
    def showDieFace(self):
        return(self.faceNum)
 
# Create a function that rolls five different dice.
# Display the roll results to the screen
def diceRoll():    
    die1 = Die(6, 1)
    die2 = Die(6, 1)
    die3 = Die(6, 1)
    die4 = Die(6, 1)
    die5 = Die(6, 1)
    
    myDice = [die1, die2, die3, die4, die5]
    
    for rolled in myDice:    
        rolled.roll()
        diceList.append(rolled.showDieFace())

# Checks to see if all five dice have the same face value. If they do, then print “YAHTZEE” to the screen.    
    for dice in diceList:
        global Yahtzee
        if diceList[0] != dice:
            Yahtzee = False
            break
        else: 
            Yahtzee = True
 
    if Yahtzee == False:
        print(diceList)
        print("No Yahtzee. Continue rolling your dice.")

    else:
        print(diceList)
        print("Yahtzee")


diceRoll()