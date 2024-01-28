#Write a Python program to accept n numbers in list and remove duplicates from a list.

a=list(map(int,input('Enter the numbers: ').split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
print('The list after removing duplicates is: ',b)
