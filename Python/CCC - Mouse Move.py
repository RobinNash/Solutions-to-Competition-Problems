# Mouse Move #
# November 12, 2018
# By Robin Nash

[c,r] = [int(i) for i in input().split(" ") if i != " "]
x,y = 0,0

while True:
    pair = [int(i) for i in input().split(" ") if i != " "]
    if pair == [0,0]:
        break
    x += pair[0]
    y += pair[1]
    pair = [x,y]
    for i in range(2):
        if pair[i] > [c,r][i]:
            pair[i] = [c,r][i]
        if pair[i] < 0:
            pair[i] = 0
    [x,y] = pair
    print(x,y)
#1541983052.0