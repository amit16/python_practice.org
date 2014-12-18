'''

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 

'''

name = raw_input("Please enter your name, Sir : ")

try:
    age =  int(raw_input("Hey! " + name + " Please enter your age(in years) : "))
except ValueError:
    print "Are you Serious..!! Please enter the age in years (numbers)"

if age == 100:
    print "Hi %s, you have already turned 100 this year, that means - 2014" %name
else:
    age_year = 2014 + (100 - age)
    print "Hi %s, you will turn 100 in the year - %d" % (name, age_year)
    
'''

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


'''

print_count = int(raw_input(name + ", How many times would you like me to print the above message for you(enter a number) :"))

for i in range(0, print_count) :
    print "\n Hi %s, you will turn 100 in the year - %d" % (name, age_year)


print "Thanks..!!"
    
    
    
