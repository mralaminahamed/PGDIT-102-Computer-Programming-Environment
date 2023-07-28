def count_down(n):
    # Print the recursion number
    print(n)

    if n > 1:
        count_down(n - 1)


if __name__ == '__main__':
    # Collect numbers from user
    num = int(input("Enter Number:"))
    # Print the count-down number
    count_down(num)
