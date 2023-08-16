# Question: Write a program that prints the perimeter of a rectangle to take its height and width as input.

# Show message to the screen for getting a rectangle's height and width.
height = int(input('Enter the height of the rectangle: '))
width = int(input('Enter the width of the rectangle: '))

# Calculate the perimeter of a rectangle and assign variable.
# formula: P = 2(a + b)
perimeter = 2 * (height + width)

# Show the output.
print("The perimeter of rectangle is : ", perimeter)
