# Sum of Even Fibonacci numbers below 4 milliions

a, b = 0, 1
list_of_fibo = []
sum = 0

for i in range(1, 40) :
    a, b = b, a + b 
    list_of_fibo.append(b)
    

for n in list_of_fibo :
    if n % 2 == 0 :
        sum = sum + n
        
if sum < 4000000 :
    print sum
else:
    print " the sum is grester than 4 million, man.!!"
        
