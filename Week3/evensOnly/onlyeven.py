#Prompt the user to enter a positive number. 
prompt = ("Please input an even number between 0 and 20: ")

def evenOnly() :        
    for x in range(0, int(userNum), 2):
        print(x)

active = True

while active:
    userNum = input(prompt)
    numCheck = userNum.isdigit()
    if numCheck == True:
        print(evenOnly())
        active = False
    else :
        print("The input is incorrect.")