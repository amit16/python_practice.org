'''
This Program converts the String into uppercase
without using any in-built methods like str.upper() 

'''

word = list(raw_input("Enter a String : "))

word_list = []

for i in range(0, len(word)):
    o = ord(word[i])
    u = o - 32 
 
 '''
 This condition statement checks whether a char is lower case or not
   If not, it will pass
   '''    
    if o >=97 and o <=122:
        word_list.append(unichr(u))
    else:
        word_list.append(word[i])
   
       
print "The String in uppercase is : " + ''.join(word_list) 
