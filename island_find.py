#Main Program Starts
#Island Problem - Find out the number of island in a snap of Map

with open('coordinates.txt') as f:
    given_coord = f.read().splitlines()


parent_list = list()
list_h = list()
list_v = list()

for i in given_coord:
    parent_list.append(tuple(i))

#parent_list_without_zero = [x for x in parent_list if x[2] != '0']
#print sorted(parent_list_without_zero)


for i in sorted(parent_list):
    if i[2] != '0':
        #list_h.append(i)
        
        crd_h_plus = (str(int(i[0]) + 1), i[1], i[2])
        if crd_h_plus[2] != '0' and crd_h_plus in parent_list:
            list_h.append(crd_h_plus)
            
        crd_h_minus = (str(int(i[0]) - 1), i[1], i[2])
        if crd_h_minus[2] != '0'and crd_h_minus in parent_list:
            list_h.append(crd_h_minus)
            
        crd_v_plus = (i[0],str(int(i[1]) + 1), i[2])
        if crd_v_plus[2] != '0'and crd_v_plus in parent_list:
            list_v.append(crd_v_plus)
            
        crd_v_minus = (i[0],str(int(i[1]) - 1), i[2])
        if crd_v_minus[2] != '0'and crd_v_minus in parent_list:
            list_v.append(crd_v_minus)
            
    #parent_list = [x for x in parent_list if x not in (list_h+list_v)]    
            
        
#print list_i   

    #while i[0] != 0 :
        #crd_h_plus = (str(int(i[0]) + 1), i[1], i[2])
        #if crd_h_plus[0] != '0' and crd_h_plus[2] != '0':
            #list_h.append(crd_h_plus)
               #break

        ##crd_h_minus = (str(int(i[0]) - 1), i[1], i[2])            
        #if crd_h_minus[0] != '0' and crd_h_minus[2] != '0':
##            list_h.append(crd_h_minus)
##               #break
##            
##new_parent_list = [x for x in parent_list if x not in list_h]
##
##
##
##for j in new_parent_list:
##    #while j[0] != 0 :
##        crd_v_plus = (j[0],str(int(j[1]) + 1), j[2])
##        if crd_v_plus[1] != '0' and crd_v_plus[2] != '0':
##            list_v.append(crd_v_plus)
##               #break
##            
##        crd_v_minus = (j[0],str(int(j[1]) - 1), j[2])
##        if crd_v_minus[1] != '0' and crd_v_minus[2] != '0':
##            list_v.append(crd_v_minus)
               #break

print sorted(list_h)
print sorted(list_v)
#islands = set(list_h+list_v)
#print sorted(list(islands))

