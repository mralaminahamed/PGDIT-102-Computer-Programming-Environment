def reverse(number):
    num = 0

    while number != 0:
        digit = number % 10
        number = number // 10
        num = num * 10 + digit

    return num

    # # Convert the number to a string and reverse it using slicing
    # reversed_str = str(number)[::-1]
    # # Convert the reversed string back to an integer
    # reversed_num = int(reversed_str)
    # return reversed_num


def palindrome_check(number):
    # Get the reversed version of the number
    reversed_number = reverse(number)

    # Check if the original number and its reversed version are the same
    if number == reversed_number:
        return True
    else:
        return False


if __name__ == '__main__':
    # Collect numbers from user
    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number:"))
    # num1 = 12321
    # num2 = 45678

    print(f"Is {num1} a palindrome? {palindrome_check(num1)}")
    print(f"Is {num2} a palindrome? {palindrome_check(num2)}")
