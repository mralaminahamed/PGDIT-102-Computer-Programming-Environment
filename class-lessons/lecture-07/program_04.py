# Write a Python script that takes input from the user and displays that
# input back in upper and lower cases based on selection.

def main():
    user_input = input("Enter a string: ")
    choice = input("Select an option (U for uppercase, L for lowercase): ").upper()

    if choice == 'U':
        print("Uppercase:", user_input.upper())
    elif choice == 'L':
        print("Lowercase:", user_input.lower())
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
