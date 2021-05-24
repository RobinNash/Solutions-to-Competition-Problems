# Mouse Journey #
# September 29, 2019
# By Robin Nash

r,c = map(int, input().split())

# 2D array to hold where cages are
cages = [[False for i in range(c+1)] for i in range(r+1)]

# 2D array to dynamically allocate the number of paths to each point
grid = [[0 for i in range(c+1)] for i in range(r+1)]

# add the cages to the cage array
for i in range(int(input())):
    y,x = map(int, input().split())
    cages[y][x] = True


grid[1][0] = 1

for y in range(1,r+1):
    for x in range(1,c+1):
        if cages[y][x]:
            continue

        # The paths to one point are the sum of the paths
        # to the points above and to the left
        grid[y][x] = grid[y-1][x] + grid[y][x-1]

# Output numbe of paths to destination
print(grid[r][c])


#1569785186.0
