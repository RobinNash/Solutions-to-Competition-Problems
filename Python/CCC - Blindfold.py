# Blindfold #
# October 27, 2018
# By Robin Nash

def getAngel(angel):
    if angel == -90:
        angel = 270
    elif angel == 360:
        angel = 0
    return(angel)

r = int(input())
c = int(input())
rows= []
newRows=[[0 for i in range(c)] for i in range(r)]
for i in range(r):
    rows.append(input())
print(newRows)

m = int(input())
moves = []
for i in range(m):
    moves.append(input())

positions = []
for y in range(r):
    for x in range(c):
        point = [x,y]
        if rows[y][x] == '.':
            positions.append(point)
            
initialDirections = [0,90,180,270]

for position in positions:
    for direction in initialDirections:
        x,y = position[0],position[1]
        end = True
        for move in moves:
            if move == "F":
                if direction == 0:
                    x += 1
                elif direction == 90:
                    y -= 1
                elif direction == 180:
                    x -=1
                elif direction == 270:
                    y +=1
                
            elif move == "R":
                direction -= 90
                direction = getAngel(direction)
                
            elif move == "L":
                direction += 90
                direction = getAngel(direction)
                
            if [x,y] not in positions:
                end = False

        if x not in range(c) or y not in range(r):
            end = False
        elif rows[y][x] != '.':
            end = False
            
        if end == True:
                newRows[y][x] = '*'

for y in range(r):
    for x in range(c):
        if newRows[y][x] == 0:
            newRows[y][x] = rows[y][x]
for row in newRows:
    for i in row:
        print(i,end='')
    print("")
    

            
            
    
#1540671374.0