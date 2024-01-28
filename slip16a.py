#Write a Python script to sort (ascending and descending order) a dictionary by key.

# Define a dictionary
my_dict = {'c': 3, 'a': 1, 'b': 2}

# Sort the dictionary in ascending order by key
sorted_dict_asc = dict(sorted(my_dict.items()))

# Sort the dictionary in descending order by key
sorted_dict_desc = dict(sorted(my_dict.items(), reverse=True))

# Print the sorted dictionaries
print("Ascending order:", sorted_dict_asc)
print("Descending order:", sorted_dict_desc)
