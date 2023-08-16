# Write a program to read the age of a candidate and determine whether s/he is
# eligible for casting vote.

# Collect the age of user from sher/him.
age = int(input("Enter your age: "))
eligible_age_for_vote = 18

if age >= eligible_age_for_vote:
    print("You are eligible for casting vote.")
else:
    print("You are not eligible for casting vote.")
