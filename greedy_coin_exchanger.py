__author__ = 'Amit'

amount = input("Enter the amount in dollar")

amount_cents = int(amount*100)

ans = []

denoms = [25, 10, 5, 1]

while amount_cents > 0:
    if amount_cents >= denoms[0]:
        num = amount_cents // denoms[0]
        amount_cents -= (num * denoms[0])
        ans.append(num)

    denoms = denoms[1:]

print "You will get :\n"
    #, sum(ans), " no. of coins as change "


print ans[0], " No. of Quarters\n", ans[1], " No. of Dimes\n", ans[2], " No. of Nickels\n", ans[3], " No. of Pennies\n"
