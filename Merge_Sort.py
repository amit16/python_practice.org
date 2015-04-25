import random

def Merge_Sort(myList):
    if len(myList)>1:
        mid = len(myList)//2
        Left_myList = myList[:mid]
        Right_myList = myList[mid:]
    
     
    
        Merge_Sort(Left_myList)
        Merge_Sort(Right_myList)
    
        i=0
        j=0
        k=0    
    
        while i < len(Left_myList) and j < len(Right_myList):
            if Left_myList[i] < Right_myList[j]:
                myList[k] = Left_myList[i]
                i += 1
            else:
                myList[k] = Right_myList[j]
                j += 1        
            k +=1
        #For the remaining items, anyone of these two loops will execute
        while i < len(Left_myList):
            myList[k] = Left_myList[i]
            i += 1        
            k += 1
        while j < len(Right_myList):
            myList[k] = Right_myList[j]
            j += 1        
            k += 1
    return myList
    
    #Using Python in-built method - merge from heapq library, we can merge more easily
    
    #we can just return merge(Left_mylist, Right_myList) after ( from heapq import merge )  
        
    

my_unsorted_list = random.sample(xrange(100),10)
print my_unsorted_list
my_sorted_list = Merge_Sort(my_unsorted_list)
print my_sorted_list
