#!/usr/bin/python

__author__ = 'Amit'

while True:
    amount = input("Enter the amount(in dollar), u need change for : ")
    if amount > 0:
        break

amount_cents = int(amount*100)
ans = []

denoms = [25, 10, 5, 1]

while amount_cents > 0:
    if amount_cents >= denoms[0]:
        num = amount_cents // denoms[0]
        amount_cents -= (num * denoms[0])
        ans.append(num)

    denoms = denoms[1:]

    
length = len(ans)

change_values = {

    0:'- Quarters',
    1:'- Dimes',
    2:'- Nickel',
    3:'- Penies',
     
}

print "You will get :"

for i in range(0, length):
    print ans[i]," ", change_values[i]
    i =-1
    
   
    
   
    

