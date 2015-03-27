__author__ = 'Amit'

amount = input("Enter the amount in dollar")

'''
if isinstance(amount, float):
    amount = amount * 100
'''


ans = []

denoms = [25, 16, 5, 1]

while amount > 0:
    if amount >= denoms[0]:
        num = amount // denoms[0]
        amount -= (num * denoms[0])
        ans.append(num)

    denoms = denoms[1:]

print "You will get ", sum(ans), " no. of coins as change "
