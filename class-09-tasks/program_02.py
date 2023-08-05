# Write a Python script to concatenate the following dictionaries to create a
# new one.

us = {"United States": "New York", }
it = {"Italy": "Naples", }
en = {"England": "London"}

# Define the dictionaries to be concatenated
country_capitals = {}
# Concatenate the dictionaries using the update() method

country_capitals.update(us)
country_capitals.update(it)
country_capitals.update(en)

print("Concatenated Dictionary:", country_capitals)
