#Write a Python program to unzip a list of tuples into individual lists.
# L= [(1,2), (3,4), (8,9)]


L = [(1, 2), (3, 4), (8, 9)]

# Unzip the list of tuples into individual lists
unzipped = list(zip(*L))

# Display the individual lists
for lst in unzipped:
    print(list(lst))
