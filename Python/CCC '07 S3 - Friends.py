# Friends again #
# March 15, 2019
# By Robin Nash

import sys

def getCircle(friend, pairs, circle):
    
    circle.append(pairs[circle[-1]])
    last = circle[-1]
    if last == circle[0]:
        return circle[:-1]
    if last in circle[:-1]:
        return circle[circle.index(last):-1]
    return getCircle(friend, pairs, circle)

def getDistance(a,b,circle):
    ai = circle.index(a)
    bi = circle.index(b)
    d1 = bi-ai-1
    d2 = len(circle) - bi + ai -1
    return min([d1, d2])
    

data = ['9', '2 3', '1 2', '3 1', '10 11', '100 10', '11 100', '12 100', '13 14','14 100', '1 100', '2 3', '12 14']
##data = sys.stdin.read().strip().split('\n')[:-1]

friendsNum = int(data.pop(0))
pairs = {f:ff for f,ff in [pair.split() for pair in data[:friendsNum]]}
checkPairs = [pair.split() for pair in data[friendsNum:]]
data.clear()


circles = []
append = circles.append
for f,ff in pairs.items():
    if circles == [] or True not in [f in c and ff in c for c in circles]:
        circle = getCircle(f,pairs,[f])
        append(circle)

##sample = [(1,2,[2,3,4,1]), (1,2,[4,5,1,0,0,0,2])]

##for a,b,circle in sample:
##    a,b = sorted([circle.index(a),circle.index(b)])
##    a,b = circle[a],circle[b]
##    print(getDistance(a,b,circle))
        
for a,b in checkPairs:
    try:
        circle = [c for c in circles if a and b in circle][0]
        distance = getDistance(a,b,circle)
        print('Yes',distance)
    except ValueError:
        print('No')
    except IndexError:
        print("No")
print(circles)
#1552666028.0