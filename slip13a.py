#Write a python script to implement selection sort using list.

def selection_sort(my_list):
    temp = 0
    for i in range(len(my_list)):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp

obj=input("Enter the list of numbers:")
my_list = obj.split()
my_list = [int(x) for x in my_list]
selection_sort(my_list)
print("Sorted list:", my_list)
