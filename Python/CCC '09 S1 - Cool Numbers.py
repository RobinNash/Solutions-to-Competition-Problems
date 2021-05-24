# Cool Numbers #
# August 20, 2019
# By Robin Nash

a = int(input())
b = int(input())


cool = [1,64,729,4096,15625,46656,117649,262144,531441,1000000,1771561,2985984,\
        4826809,7529536, 11390625, 16777216, 24137569, 34012224, 47045881,\
        64000000, 85766121] # 5 dec

total = 0
for x in cool:
    if a <= x <= b:
        total += 1

    if x > b:
        break

print(total)


##for x in range(a, b+1):
##    if round(x**(1/3),3) % 1 == 0 and round(x**.5,3) % 1 == 0:
##        if x not in cool:
##            print(x, round(x**(1/3),2), round(x**.5,2))
##            cools.append(x)


coool = [1, 64, 729, 4096, 15625, 46656, 117649, 262144, 531441, 1000000, 1771561, 2985984, 4826809, 7529536, 11390625, 16777216, 24137569, 34012224, 47045881, 64000000, 85766121]

#print (cool == coool) #it returned True
# cool is rounded to 5, cools (3 dec) returned no new numbers, only false ones
#1566324144.0