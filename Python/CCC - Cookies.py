# Cookies #
# November 12, 2018
# By Robin Nash

def getFurthestPoints(chips):
    d = 0
    for a in chips:
        for b in chips:
            if distance(a,b)>d:
                d = distance(a,b)
                A = a
                B = b
    return A,B

def getFurthestPoint(a,notThesePoints,chips):
    d = 0
    for b in [i for i in chips if i not in notThesePoints]:
        if distance(a,b)>d:
            d = distance(a,b)
            c = b
    return c

def negRec(a,b):
    try:
        return -1*(a[0]-b[0])/(a[1]-b[1])
    except ZeroDivisionError:
        return 0

def mid(a,b):
    return [(a[0]+b[0])/2,(a[1]+b[1])/2]

def yint(a,slope):
##    if slope != 0:
    return a[1]-slope*a[0]



def distance(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

chips = []
for i in range(int(input())):
    chips.append([int(i) for i in input().split(" ") if i != " "])

a,b = getFurthestPoints(chips)
c = getFurthestPoint(mid(a,b),[a,b],chips)

if a[1] == b[1]:
    a,b = c,b
elif b[1] == c[1]:
    b,c = a,c
elif c[1] == a[1]:
    a,c = a,b

for i in [b,c]:
    print(negRec(a,i),yint(mid(a,i),negRec(a,i)))


m1 = negRec(a,b)
m2 = negRec(a,c)
b1 = yint(mid(a,b),negRec(a,b))
b2 = yint(mid(a,c),negRec(a,c))
slopes = [m1,m2]

if m1 == 0 and m2 == 0:
    m2 = negRec(b,c)
    b2 = yint(mid(b,c),m2)
    slopes = [m1,m2]
if 0 not in slopes:
    x = (b2 - b1) / (m1 - m2)
    y = negRec(a,b)*x + yint(mid(a,b),negRec(a,b))
elif 0 in slopes:
    if m1==0:
        y = m2*b1+b2
        x = b1
    elif m2==0:
        y = m1*b2+b1
        x = b2

origin = [x, y]
diameter = distance(a,origin)*2
print("%.2f"%diameter)



#ab : y = negRec(a,b)x+ yint(mid(a,b),negRec(a,b))
#ac : y = negRec(a,c)x+ yint(mid(a,c),negRec(a,c))
#negRec(a,b)x+ yint(mid(a,b),negRec(a,b)) = negRec(a,c)x+ yint(mid(a,c),negRec(a,c))
#negRec(a,b)*x - negRec(a,c)*x =yint(mid(a,c),negRec(a,c))-yint(mid(a,b),negRec(a,b))
##for b in [b,c]:
##    print (negRec(a,b),yint(mid(a,b),negRec(a,b)))
#1541982020.0