#Write a Python program to accept n numbers in list and remove duplicates from a list.

def duplicate(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

arr=input("List of numbers: ")
arr=arr.split()
arr=[int(i) for i in arr]
print("New list: ",duplicate(arr))
