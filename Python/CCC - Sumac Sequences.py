# Sumac Sequences #
# November 29, 2018
# By Robin Nash

x = int(input())
y = int(input())

sumac = [x,y]

while True:
    sumac.append(sumac[len(sumac)-2]-sumac[len(sumac)-1])
    if sumac[-2] < sumac[-1]:
        break

print(len(sumac))
#1543452642.0