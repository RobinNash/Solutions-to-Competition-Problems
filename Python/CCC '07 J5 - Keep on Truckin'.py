# Keep on Truckin' #
# December 18, 2019
# By Robin Nash



motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]


dmin = int(input())
dmax = int(input())

for i in range(int(input())):
    motels.append(int(input()))

motels.sort()


#store in each dp cell how many ways are there to travel to that cell

dp = [0 for i in range(len(motels))]
dp[0]=1
for i in range(1,len(motels)):
    for j in range(i-1,-1,-1):
        dis = motels[i]-motels[j]
        if dis > dmax:
            break
        if dis >= dmin:# and dp[j]!=0:
            dp[i] += dp[j]

print(dp[-1])
    
    
#1576713594.0