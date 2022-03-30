# Prompt the user to input a number.
userNumber = int(input("Please type in your number "))
print(f"input: {userNumber}")
# Multiple this number by 3.
multiply = int(userNumber * 3)
# Add 6 to the number
add = int(multiply + 6)
# Divide the new number by 3.
divide = int(add / 3)
# Subtract the number from step 1 from the answer in step 4.
print(f"output: {divide - userNumber}")
# Display the results as an integer.  The results should always be 2. 