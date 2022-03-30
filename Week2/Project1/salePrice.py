# Prompt the user to enter a description for a product.
userProduct = input("Please enter your product. ")
print(userProduct)
# Prompt the user to enter the quantity being purchased.
# Be sure to display the product to the user during the prompt.
# Store the value as an integer.
userQuantity = int(input("How many would you like to purchase? "))
print(f"{userProduct} x {userQuantity}.")
# Prompt the user to enter the regular price of the product. This value must be stored as a float.
regPrice = float(input("What is the regular sales price per item? "))
# All of the products over $19.99 are 15% OFF
# All of the products over $39.99 are 25% OFF
if regPrice > 19.99 and regPrice < 39.99: 
    orgPrice = regPrice
    regPrice = regPrice - (regPrice * .15)  
    print(f"Your new price after the savings is {regPrice:.2f} per item.")
    # Display the total amount saved.
    print(f"You Saved {((orgPrice - regPrice) * userQuantity):,.2f}.")
elif regPrice > 39.99:
    orgPrice = regPrice
    regPrice = regPrice - (regPrice * .25)
    print(f"Your new price after the savings is {regPrice:.2f}.")
    # Display the total amount saved.
    print(f"You Saved {((orgPrice - regPrice) * userQuantity):,.2f} per item.")
# Calculate the sales tax on the total purchase.
# Assume a state sales tax rate of 6.5%.
# The rate should be calculated on the total price of the products after discount savings.
# Store this value as float in a variable.
salesTax = (regPrice * userQuantity) * .065 
print(f"Your sales tax is {salesTax:.2f}.") 
# Display the total amount due from the customer.
# Format the output as a fixed point number with two-decimal places, a comma as a thousand separator and the dollar sign.
totalPrice = (regPrice * userQuantity) + salesTax
print(f"Your total price after tax is ${totalPrice:,.2f}.")

