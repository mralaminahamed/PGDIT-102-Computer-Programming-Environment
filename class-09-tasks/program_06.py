# Write a Python program to read first line of a file.

file = open('read-file.txt', 'a')
file.write('This is next line\n')
file.close()

updated_file = open('read-file.txt', 'r')
print(updated_file.read())
updated_file.close()
