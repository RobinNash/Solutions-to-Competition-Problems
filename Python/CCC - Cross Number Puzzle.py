# Cross Number Puzzle #
# November 19, 2018
# By Robin Nash

##perfectNumbers = [x for x in range(1000,10000) if x == sum([i for i in range(1,x) if x%i==0])]
print(8128)


##cubes = [x for x in range(100,1000) if x == sum([int(str(x)[i])**3 for i in range(3)])]
cubes = [153, 370, 371, 407]
for i in cubes:
    print(i,end=' ')
#1542595730.0