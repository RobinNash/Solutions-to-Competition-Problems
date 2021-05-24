# Time on Task
# January 22, 2021
# By Robin Nash
# Jan 22 2021


minutes = int(input())

n = int(input())

data = [int(input()) for i in range(n)]

data.sort(reverse = True)
data.pop(0)

chores = -1
while minutes >= 0:
    minutes -= data.pop()
    chores += 1
print(chores)
#1611347301.259312