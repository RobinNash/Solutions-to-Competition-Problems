# Roll the Dice #
# November 17, 2018
# By Robin Nash

n = int(input())
m = int(input())

if n > 10:
    n = 9
if m > 10:
    m = 9

ways = 0
for n in range (1,n+1):
    for m in range(1,m+1):
        if n + m == 10:
            ways+=1

if ways == 1:
    print("There is 1 way to get the sum 10.")
else:
    print("There are",ways,"ways to get the sum 10.")
#1542488930.0