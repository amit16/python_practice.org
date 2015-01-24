import random

def swape_indices(myLi, index1, index2):
    tmp = myLi[index1] 
    myLi[index1] = myLi[index2]
    myLi[index2] = tmp
    
    
    
def selection_sort(myList):
    
    for i in range(len(myList)):
        smallest = i
            
        for j in range(i+1, len(myList)):
            if myList[j] < myList[smallest] :
                smallest = j
        
        swape_indices(myList,smallest, i)
        
    return myList          
   
        
    
my_unsorted_list = random.sample(xrange(10000),1000)
print my_unsorted_list
my_sorted_list = selection_sort(my_unsorted_list)
print my_sorted_list

# For printing in increasing order, replace the '<' sign with '>'




    
