# Write a program to accept a coordinate point in a XY coordinate system and
# determine in which quadrant the coordinate point lies.

# x == 0 or y == 0 = on the axis not any coordinate
# x > 0 or y > 0, 1st
# x neg

# Collect the coordinate points for x and y.
xCoordinate = float(input('Enter the coordinate point of X:'))
yCoordinate = float(input('Enter the coordinate point of Y:'))

# Determine the quadrant the coordinate point lies.
if xCoordinate > 0 and yCoordinate > 0:
    print('1st coordinate.')
# elif xCoordinate < 0 and yCoordinate > 0:
elif xCoordinate < 0 < yCoordinate:
    print('2nd coordinate.')
elif xCoordinate < 0 and yCoordinate < 0:
    print('3st coordinate.')
# elif xCoordinate > 0 and yCoordinate < 0:
elif xCoordinate > 0 > yCoordinate:
    print('4th coordinate.')
