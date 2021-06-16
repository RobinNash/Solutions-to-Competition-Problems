# Super Plumber #
# December 30, 2019
# By Robin Nash

import sys

data = sys.stdin.read().split('\n')

h,w = map(int,data.pop(0).split())
while (h,w) != (0,0):
    
    # Holds the map + a surrounding wall to avoid index errors
    grid = [['-']*(w+2)]+[["-"]+[i for i in data.pop(0)]+["-"] for i in range(h)]+[['-']*(w+2)]

    # Builds more walls:
    #if you got something like:  you'll wanna make it:
    # .**    .**
    # *.. -> ***
    # *.. -> ***
    # .**    .**
    for x in range(1,1+w):
        floor = False
        wall =[False for i in range(h+2)]
        for y in range(h,0,-1):
            if [x,y] == [1,h]:
                continue
            if grid[y][x] == '*':
                if not floor:
                    floor = True
                else:

                    for i in range(h+2):
                        if wall[i]:
                            grid[i][x] = '*'
            elif floor and grid[y][x-1] == '*':
                wall[y] = True
            if grid[y][x-1] != '*' and grid[y][x]!='*':
                floor = False
                wall =[False for i in range(h+2)]

    # will hold the max money for each cell
    dp = [[0 for i in range(w+2)] for i in range(h+2)]

    # holds the money value for each cell (static)
    values = [[0 for i in range(w+1)] for i in range(h+2)]

    # Append values to values array 
    for y in range(h,0,-1):
        for x in range(1,w+1):
            if grid[y][x].isdigit():
                values[y][x] = int(grid[y][x])

    # For each move right, we'll go up all the way then down all the way
    for x in range(1,w+1):

        # Array of values for current column if from the bottom to the top
        up = [0 for i in range(h+2)]
        for y in range(h,0,-1):
            if grid[y][x]!='*':

                # Builds wall if there is a floor and wall on either side,
                # because if you go down into it, the only way out is up and that's a no-no
                if [grid[y+1][x],grid[y][x+1],grid[y][x-1]] ==['*','*','*']:
                    grid[y][x] = '*'
                    
                else:
                    up[y] = max([dp[y][x],up[y+1],dp[y][x-1]])+values[y][x]

        # Array of values if top to bottom
        down= [0 for i in range(h+2)]
        for y in range(1,h+1):
            if grid[y][x]!='*' and x!=1:
                # Builds wall if there is roof and wall on either side
                if [grid[y-1][x],grid[y][x+1],grid[y][x-1]] ==['*','*','*']:
                    grid[y][x] = '*'
                else:
                    down[y] = max([dp[y][x],down[y-1],dp[y][x-1]])+values[y][x]

        # For each cell, use biggest value if going up or down for that cell,
        # not all cells have to have same vertical direction
        for y in range(1,h+1):
            dp[y][x] = max([down[y],up[y]])

    print(dp[h][w])
    
    h,w = map(int,data.pop(0).split())

        
'''
12 12
............
.......*9*..
..*****99*..
....8.****..
.....8*..7..
....8.*.27..
....*******.
....8.....*.
...**...8.*.
...8*.*****.
...**.8...*.
........8.*.
0 0
'''#0


##    p(grid)
##    p(dp)
##h,w = 5, 10
##grid = ['************', '*..3.......*', '*..........*', '*..7.**....*',\
##        '*.9**...1..*', '*..8..9....*', '************']

#5 test cases 3,4 answers 24, 183
#1577732838.0
