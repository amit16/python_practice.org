def Search(list_elements, element):
    l = len(list_elements)
    upper = l-1
    lower = 0
    
    while upper >= lower:
        middle = (upper + lower)/2
        
        if list_elements[middle] == element:
            return True
        elif list_elements[middle] < element:
            lower = middle + 1
        elif list_elements[middle] > element:
            upper = middle - 1
            
    return False    
    
    
values = input("Enter the list of elements")

value = input("Enter the value to be searched")

list_sorted = sorted(values)

result = Search(list_sorted, value)

if result == True:
    print "element found"
else:
    print "element not found"





 
