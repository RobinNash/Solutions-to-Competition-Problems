# Maze #
# January 25, 2020
# By Robin Nash


for t in range(int(input())):
    r = int(input())
    c = int(input())
    maze = [input() for i in range(r)]
    
    maze = ["*"*(c+2)]+["*"+i+"*" for i in maze]+["*"*(c+2)]

    nxt = [[[] for i in range(c+2)]for i in range(r+2)]
    prev = [[[] for i in range(c+2)]for i in range(r+2)]
    dp = [[0 for i in range(c+2)]for i in range(r+2)]
    vis = [[False for i in range(c+2)]for i in range(r+2)]

    dp[1][1] = 1


    for y in range(1,r+1):
        for x in range(1,c+1):
            inter = maze[y][x]
            if inter == "*":
                continue
            
            n = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
            for [a,b] in n[2:]:
                ns = maze[b][a]
                if ns == "|" or ns == "+":
                    prev[y][x].append([a,b])
            for [a,b] in n[:2]:
                we = maze[b][a]
                if we == "-" or we == "+":
                    prev[y][x].append([a,b])
                    
            if inter == "|":
                n = n[2:]
            elif inter == "-":
                n = n[:2]

            for p in n:
                nxt[y][x].append(p)
            
    queue = nxt[1][1]
    for [x,y] in nxt[1][1]:
        vis[y][x] = True

    while queue!= []:
        [x,y] = queue.pop(0)
        try:
            dp[y][x] = min([dp[b][a]+1 for [a,b] in prev[y][x] if dp[b][a]])
        except ValueError:
            pass
        
        for [a,b] in nxt[y][x]:
            if not vis[b][a]:
                vis[b][a] = True
                queue.append([a,b])

    if dp[r][c] == 0:
        print(-1)
    else:
        print(dp[r][c])
           
# this is for testing, prints an array in a readable way
def pdp(a):
    for y in a[1:-1]:
        print(" ".join([str(i) for i in y[1:-1]]))
#1579982180.0