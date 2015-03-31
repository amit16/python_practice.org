#Bubble Sort Implementation in Python


import random
def Bubble_Sort(list_elements):
    l = len(list_elements)
    temp = None
    while True:
        count = 0
        k = 0
        for i in range(0, l-1-k): 
        '''
        k is used to remove the last element from every iteration
        as it is already sorted
        
        ''' 
            if list_elements[i] > list_elements[i+1]:       
                list_elements[i],list_elements[i+1]  = list_elements[i+1], list_elements[i]
                count += 1
            k +=1
        if count <= 0:
            break;
            
    return list_elements
        
    
#values = input("Enter the list of elements to be sorted :")

values = [int(1000*random.random()) for i in xrange(50)]

result = Bubble_Sort(values)

print "Sorted List is : ", result





 
