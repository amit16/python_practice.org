'''
Problem Statement :
You are given three integers X, Y and Z denoting the dimensions of a Cuboid.
You have to print a list of all possible coordinates on the three dimensional grid, 
such that at any point the sum Xi + Yi + Zi is not equal to N. If X = 2, 
then possible values of Xi can be 0, 1 and 2. The same applies to Y and Z.

Input Format :

Four integers X, Y, Z and N in four different lines.

Output Format :

You have to print the list, in increasing order.

'''

X,Y,Z,N = input(), input(), input(), input()

list_X = [x for x in range(0, X+1)]
list_Y = [y for y in range(0, Y+1)]
list_Z = [z for z in range(0, Z+1)]

coordinates = [[i, j, k] for i in list_X for j in list_Y for k in list_Z]

'''
#Without Above List Comprehension :-

for i in list_X:
    for j in list_Y:
        for k in list_Z:
            coordinates.append([i, j, k])
'''

main_list = [entry for entry in coordinates if sum(entry) != N]
print sorted(main_list)
