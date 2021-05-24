flips = input().replace('VV','')
# February 20, 2019
# By Robin Nash
flips = flips.replace('HH','')

grid = [['1','2'],['3','4']]

for flip in flips:
    if flip == 'H':
        grid.reverse()
    elif flip == 'V':
        grid[0].reverse()
        grid[1].reverse()

for row in grid:
    print(' '.join(row))
#1550672260.0