# Double Dice #
# March 12, 2019
# By Robin Nash

antonia = 100
david = 100


for i in range(int(input())):
    a, d = [int(roll) for roll in input().split()]
    if a < d:
        antonia -= d

    if d < a:
        david -= a

print(antonia)
print(david)
#1552424108.0