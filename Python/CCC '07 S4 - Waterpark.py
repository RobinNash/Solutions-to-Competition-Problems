# Water park
# December 26, 2020
# By Robin Nash


# Create list of list of all nodes above and connected to node of that index
# [[],[],[1],[2],[1,2,3]]
# Create a list of paths to take to each (store sum of dp of upper nodes)
# [0,1,1,1,3]

n = int(input())
edges = [[] for i in range(n+1)]
dp = [0 for i in range(n+2)]
dp[1] = 1

# Create graph
while True:
    a,b = map(int,input().split())
    if (a,b) == (0,0):
        break
    edges[b].append(a)

# Dynamically allocate paths to each node
for i in range(2,n+1):
    for x in edges[i]:
        dp[i] += dp[x]

print(max(dp[2:]))

#1609013562.1619575
