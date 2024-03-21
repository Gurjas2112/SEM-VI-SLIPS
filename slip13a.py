#Write a python script to implement selection sort using list.

#def selection_sort(my_list):
    #temp = 0
    #for i in range(len(my_list)):
        #min_index = i
        #for j in range(i + 1, len(my_list)):
            #if my_list[min_index] > my_list[j]:
                #min_index = j
        #temp = my_list[i]
        #my_list[i] = my_list[min_index]
        #my_list[min_index] = temp

#obj=input("Enter the list of numbers:")
#my_list = obj.split()
#my_list = [int(x) for x in my_list]
#selection_sort(my_list)
#print("Sorted list:", my_list)


#Write a python script to implement bubble sort using list.   

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
           
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Test the bubble sort implementation
if __name__ == "__main__":
    
    my_list = input("Enter the list of numbers: ").split()
    my_list = [int(x) for x in my_list]
    
    
    
    print("Original list:", my_list)
    
    bubble_sort(my_list)
    
    print("Sorted list:", my_list)

