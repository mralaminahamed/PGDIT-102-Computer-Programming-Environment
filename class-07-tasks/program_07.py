def reverse(number):
    # Convert the number to a string and reverse it using slicing
    reversed_str = str(number)[::-1]
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)
    return reversed_num


def palindromeCheck(number):
    # Get the reversed version of the number
    reversed_number = reverse(number)

    # Check if the original number and its reversed version are the same
    if number == reversed_number:
        return True
    else:
        return False


if __name__ == '__main__':
    num1 = 12321
    num2 = 45678

    print(f"Is {num1} a palindrome? {palindromeCheck(num1)}")
    print(f"Is {num2} a palindrome? {palindromeCheck(num2)}")