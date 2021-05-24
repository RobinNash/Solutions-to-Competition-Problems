# Deficient, Perfect, and Abundant #
# November 18, 2018
# By Robin Nash

for i in range(int(input())):
    x = int(input())
    summy = sum([i for i in range(1,x) if x%i==0])
    if summy < x:
        print(x,"is a deficient number.")
    elif summy == x:
        print(x,"is a perfect number.")
    else:
        print(x,"is an abundant number.")
    
#1542560966.0