import pickle
#Write a Pickle python program to write and read a data from a file stating the
#position of the file object. (Using dump(), load() functions).

# Write data to file
data = [1, 2, 3, 4, 5]
with open('data.pkl', 'wb') as file:
	pickle.dump(data, file)

# Read data from file
with open('data.pkl', 'rb') as file:
	loaded_data = pickle.load(file)

print(loaded_data)
