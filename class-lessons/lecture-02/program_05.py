# Question: Write a program that calculates the area of a circle.

# Show message to the screen for getting radius of a circle.
radius = int(input('Enter the radius of the circle: '))

# Set the default value for pi
PI = 3.1416

# Calculate the area of a circle, and assign variable.
# formula: A=πr2
area = PI * (radius * radius)

# Show the output.
print("The area of a circle is : ", area)
