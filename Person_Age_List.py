myList = []

num = input("Number of persons in the room :")

print "Enter ages of people in the room :"

for i in range(0, num):
    x = raw_input()
    myList.append(x)

print "Time Passes......"
print "So after 1 year age of each person in the room will be"

for n in range(0, num):
    age = myList[n] + 1
    print age

    
