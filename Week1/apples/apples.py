customerName = input("please enter your name ")
applePrice = .50
appleCount = input("Hi {}. Apples cost ${:.2f} each. How many would you like to buy? ".format(customerName, applePrice))
print("Thank you {} for your purchase of {} apples at a cost of ${:.2f} each.".format(customerName, appleCount, applePrice))

