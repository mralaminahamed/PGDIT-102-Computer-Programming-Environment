# Take input of age of 3 people by user and determine oldest and youngest
# among them.

# Collect age of 3 people.
person_01_age = int(input("Enter the age of person one: "))
person_02_age = int(input("Enter the age of person two: "))
person_03_age = int(input("Enter the age of person three: "))

# Calculate the oldest age.
oldest = ''
if person_01_age > person_02_age:
    oldest = person_01_age
else:
    oldest = person_02_age

if person_03_age > oldest:
    oldest = person_03_age

# Calculate the youngest age.
youngest = ''
if person_01_age < person_02_age:
    youngest = person_01_age
else:
    youngest = person_02_age

if person_03_age < youngest:
    youngest = person_03_age

print("The oldest person is ", oldest, 'years old')
print("The youngest person is ", youngest, 'years old')
