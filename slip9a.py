#Write a python script to find the repeated items of a tuple. tup=(1,2,2,3,4,4)

tup=(1,2,2,3,4,4)
print(tup)
print("Repeated items are:")
for i in tup:
	if tup.count(i) > 1:
		print(i, end=" ")

