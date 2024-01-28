#Write a python program to print the contents of file in reverse order.

# Open file in read mode

file = open('report.txt', 'r')

# Read data from file

data = file.read()

# Reverse data

data = data[::-1]

# Print data

print(data)

file.close()
