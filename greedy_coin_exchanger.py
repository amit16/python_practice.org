__author__ = 'Amit'

'''
Its a coin exchanger, it asks the user for an amount in dollars,
then calculates the least number of coins required in exchange of that
"Uses Greedy Algorithm"
'''

amount = input("Enter the amount(in dollar), u need change for : ")
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
