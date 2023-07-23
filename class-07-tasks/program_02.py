def is_number_in_range(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound


if __name__ == '__main__':
    # Call the function to collect numbers from the user
    num = float(input("Enter a number: "))

    # Get the range bounds from the user
    lower_number = float(input("Enter the lower bound of the range: "))
    upper_number = float(input("Enter the upper bound of the range: "))

    # Check if each collected number falls within the specified range
    if is_number_in_range(num, lower_number, upper_number):
        print(f"{num} falls within the range [{lower_number}, {upper_number}]")
    else:
        print(f"{num} does not fall within the range [{lower_number}, {upper_number}]")
