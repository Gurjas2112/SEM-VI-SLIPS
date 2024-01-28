#Write a Python program to accept two lists and merge the two lists into list of tuple.

a=list(map(int,input("Enter the first list: ").split()))
b=list(map(int,input("Enter the second list: ").split()))
c=[]
for i in range(len(a)):
    c.append((a[i],b[i]))
print("The merged list of tuple is: ",c)
