# Super Plumber #
# November 26, 2020
# By Robin Nash
# November 26 2020 #

y,x = r,c = 6,5

data = []
##for i in range(y):
##    data.append(input())

##data = ['..3.......', '..........', '..7.**....', '.9**...1..', '..8..9....']

grid = [\
'.**.1',\
'.*9..',\
'.5...',\
'.....',\
'.....',\
'.....',]

x,y = c,r = 4,4
grid = [\
'...1',\
'..9.',\
'.5..',\
'....']

grid = ['*'*(x+2)]+['*'+row+'*' for row in grid]+['*'*(x+2)]


def buildWallDown(grid,r=1,c=1):
    if r == len(grid)-1:
        return grid
    if c == len(grid[0])-1:
        return buildWallDown(grid,r+1,1)
    if grid[r][c-1] ==  grid[r][c+1] == grid[r-1][c] == '*':
        grid[r] = grid[r][:c]+'*'+grid[r][c+1:]
    return buildWallDown(grid,r,c+1)

def buildWallUp(grid,r=r,c=1):
    if r == 0 and c == len(grid[0])-1:
        return grid
    if c == len(grid[0])-1:
        return buildWallUp(grid,r-1,1)
    if grid[r][c-1] ==  grid[r][c+1] == grid[r+1][c] == '*':
        grid[r] = grid[r][:c]+'*'+grid[r][c+1:]

    return buildWallUp(grid,r,c+1)

def buildWallUp(grid,y=r-1,x=1):
    if x == len(grid[0])-1:
        return grid
    if x == len(grid[0])-2 and y==len(grid)-2: #Skip last cell
        y -= 1
    if y == 0:
        return buildWallUp(grid, r, x+1)
    if grid[y][x-1] ==  grid[y][x+1] == grid[y+1][x] == '*':
        grid[y] = grid[y][:x]+'*'+grid[y][x+1:]
    return buildWallUp(grid,y-1,x)

def buildWalls(grid,y=r-1,x=1,up = True):
    if x == len(grid[0])-1:
        return grid if not up else buildWalls(grid,y=1,x=1,up=False)
    if x == len(grid[0])-2 and y==len(grid)-2 and up: #Skip last cell up
        y -= 1
    if y == 0 or y == r+2:
        return buildWalls(grid, r if up else 1, x+1,up)
    if grid[y][x-1] ==  grid[y][x+1] == grid[y-1 + 2*int(up)][x] == '*':
        grid[y] = grid[y][:x]+'*'+grid[y][x+1:]
    return buildWalls(grid,y+1 -2*int(up),x,up)

dp = [[0 for i in grid[0]] for y in grid]



def dynamic(dp,x=1):
    if x == len(grid)-1:
        return dp
    up = [0 for i in range(len(dp))]
    down = up[:]
    for y in range(1,len(grid)-1):
        if grid[y][x] == '*':
            continue
        down[y] = dp[y][x-1]+down[y-1]+int(grid[y][x]) if grid[y][x].isdigit() else 0
    for y in range(len(grid)-2,0,-1):
        if grid[y][x] =='*':
            continue
        up[y] = dp[y][x-1]+up[y+1]+ int(grid[y][x]) if grid[y][x].isdigit() else 0
    for y in range(1,len(grid)-1):
        dp[y][x] = max(up[y],down[y])
##    print(up)
    print(down)
    return dynamic(dp,x+1)


##grid = buildWallDown(grid)
grid = buildWalls(grid)
dp = dynamic(dp)
for y in range(len(grid)):
##    print("".join(row))
    print("".join(map(str,dp[y])))
##int('*') if '*'.isdigit() else 0
    
#1606431716.206388