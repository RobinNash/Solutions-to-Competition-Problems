# Dressing Up #
# August 13, 2019
# By Robin Nash

h = int(input())

for i in range(h):
    if i > h//2:
        bow = h-i-1
    else:
        bow = i

    bow = bow*2 + 1

    space = h*2 - bow*2

    for i in range(bow):
        print('*', end = '')

    for i in range(space):
        print(' ',end = '')

    for i in range(bow):
        print('*', end='')

    print()
#1565734134.0