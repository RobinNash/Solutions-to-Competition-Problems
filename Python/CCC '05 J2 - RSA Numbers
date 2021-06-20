# RSA Numbers #
# June 19, 2021 #
# By Robin Nash #

from math import sqrt

'''
16
1 2 4 8 16
if n is a factor of k, then the pair of factors is (n, k//n)
pairs of factors checking from 1 up to k: (for n in range(1,k+1))
16: (1, 16), (2, 8), (4, 4), (8, 2), (16, 1)

n is a divisor of k
if n < sqrt(k), k/n > sqrt(k) then there is a divisor s > sqrt(k)
butttt if n == sqrt(k), then k/n = n, it's the same divisor
Therefore the number of divisors of any number k is 
2*(the number of divisors < sqrt(k)) + (1 if k is a perfect square)

What variables will we need?

first = first number in the range
last = last number in the range
(this range is inclusive)
result # number of rsa numbers in range
n # current number (defined in for loop)

for each number in the range:
divisors
'''

first = int(input())
last = int(input())

rsa = 0
for n in range(first, last+1):

    divisors = 0 

    # perfect squares have an odd number of divisors
    # 4 is an even number, so if it's a perfect square,
    # don't count it
    if int(sqrt(n))**2 == n:
        continue
    
    for d in range(1, int(sqrt(n))+1):
        
        # check if d is a divisor of n
        if n % d == 0:
            
            # add 2 to divisors
            divisors += 2 # not true if d is the sqrt(n)
            
        # if divisors > 4, it's not an rsa number
        if divisors > 4:
            break

    # check if divisors is 4
    # check if n is rsa given the divisors
    if divisors == 4:
        # increment result
        rsa += 1

print("The number of RSA numbers between",first, "and", last, "is", rsa)
