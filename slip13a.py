#Write a python script to implement bubble sort using list.

def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1
list1=[19,2,31,45,6,11,121,27]
print("Sorted list:",bubble_sort(list1))
