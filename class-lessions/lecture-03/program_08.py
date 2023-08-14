# A shop will give discount of 10% if the cost of purchased quantity is more than
# 1000. the cost from quantity with unit price 100.

# Collect the quantity of purchase from user.
quantity = int(input("Enter the quantity of purchase:"))

# Calculate the cost from quantity with unit price 100.
totalCost = quantity * 100

# Assign variable for discount price.
discountedCost = totalCost

# Show the discount availability message to the screen.
if totalCost > 1000:
    discountedCost = totalCost * .9

print('Please pay tk: ', discountedCost)
