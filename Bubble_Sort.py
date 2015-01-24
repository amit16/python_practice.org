import random
 
    
def bubble_sort(myList):
    
    for i in range(len(myList)-1, 0, -1):
        for j in range(i):
            if myList[j] > myList[j+1] :
                tmp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = tmp
        
    return myList          
   
        
    
my_unsorted_list = random.sample(xrange(100),100)
print my_unsorted_list
my_sorted_list = bubble_sort(my_unsorted_list)
print my_sorted_list
