#Write a Python program to convert a tuple of string values to a tuple of
#integer values.
#Original tuple values: (('44', '444'), ('1516', '45')) New tuple values: ((44, 444), (1516, 45))

def convert_tuple(tup):
	new_tup = ()
	for i in tup:
		new_tup += (int(i[0]), int(i[1])),
	return new_tup

tup = (('44', '444'), ('1516', '45'))
print("Original tuple values:", tup)
print("New tuple values:", convert_tuple(tup))

