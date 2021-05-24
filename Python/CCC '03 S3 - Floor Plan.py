# Floor Plan #
# December 23, 2019
# By Robin Nash

import sys

#inputs
floor = sys.stdin.read().split('\n')
flooring,r,c = map(int,[floor[0],floor[1],floor[2]])
floor = ['I'*(c+2)]+['I'+i+'I' for i in floor[3:floor.index('')]]+['I'*(c+2)]

#stores which cells have or havent been visited
vis = [[False for i in range(c+2)]for i in range(r+2)]

#makes a list of connected floors for each coordinate
links = [[[] for i in range(c+2)]for i in range(r+2)]
for y in range(1,r+1):
    for x in range(1,c+1):
        if floor[y][x]=='.':
            for a,b in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                if floor[b][a] == '.':
                    links[y][x].append([a,b])



room = 0
rooms = []
#if there are still links, there are more floors
while links != [[[] for i in range(c+2)]for i in range(r+2)]:

    #start a new floor
    room+=1
    rooms.append(1)
    queue = []
    
    #finds first link and sets it as queue
    for y in range(1,r+1):
        pairs = [i for i in links[y] if i!=[]]
        if pairs!=[]:
            x = links[y].index(pairs[0])
            queue = [[x,y]]
            vis[y][x] = True
            break

    #loop will exit once all links on one floor are cleared from links list
    #finds how many squares are in current floor and keeps it in rooms list 
    while queue != []:
        x,y = queue.pop(0)
        if not vis[y][x]:
            vis[y][x] = True
            rooms[-1]+=1
        for cell in links[y][x]:
            a,b = cell
            if not vis[b][a]:
                vis[b][a] = True
                rooms[-1]+=1
                queue += links[b][a]
                #remove link
                links[b][a] = []
            #remove link
            links[y][x] = []


#finds how many floors it covers and how much left over there is
rooms.sort(reverse = True)
floors = 0
for room in rooms:
    if flooring - room >=0 and room != 0:
        floors +=1
        flooring -= room
    else:
        break

#for some reason dmoj wants it to be "room" if there's one room even though
#that contradicts the CCC test data but okay
if floors != 1:
    print(floors,"rooms,",flooring,"square metre(s) left over")
else:
    print(floors,"room,",flooring,"square metre(s) left over")
#1577126036.0