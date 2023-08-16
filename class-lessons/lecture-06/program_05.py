# Write a program to find area of surface based on a selection
PI = 3.1416

def area_of_circle(r):
    area = PI * r * r
    return area


def area_of_rectangle(l, w):
    area = l * w
    return area


def area_of_square(b):
    area = b * b
    return area


if __name__ == '__main__':
    print("Press 1 to calculate area of circle, 2 to calculate area for rectangle, 3 to calculate area of square:")
    selection = int(input(""))

    if selection == 1:
        radius = float(input("Enter radius:"))
        result = area_of_circle(radius)
        print("Area of the circle is: ", result)
    elif selection == 2:
        length = float(input("Enter length:"))
        width = float(input("Enter width:"))
        result = area_of_rectangle(length, width)
        print("Area of the rectangle is: ", result)
    elif selection == 3:
        side = float(input("Enter side:"))
        result = area_of_square(side)
        print("Area of the square is: ", side)
    else:
        print("Invalid selection. ")
