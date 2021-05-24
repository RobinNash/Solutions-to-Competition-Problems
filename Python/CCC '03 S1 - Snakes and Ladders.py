# Snakes and Ladders #
# March 10, 2019
# By Robin Nash


import sys

snl = {54:19, 90:48, 99:77, 9:34, 40:64, 67:86}

rolls = sys.stdin.read().strip().split('\n')

rolls = map(lambda x: int(x), rolls)

square = 1
for roll in rolls:
    if roll == 0:
        print('You Quit!')
        break

    if roll + square in snl:
        square = snl[roll+square]
        
    elif roll + square <= 100:
        square += roll

    print('You are now on square',square)
    if square == 100:
        print('You Win!')
        break
#1552243370.0