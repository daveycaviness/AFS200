#Prompt the user to enter a positive number. 
prompt = ("Please input an even number: ")
x = prompt
def evenOnly() :        
    for x in range(0, 20, 2):
        print(x)

active = True

while active:
    userNum = input(prompt)
    numCheck = userNum.isdigit()
    if numCheck == True:
        evenOnly()
        active = False
    else :
        print("The input is incorrect.")