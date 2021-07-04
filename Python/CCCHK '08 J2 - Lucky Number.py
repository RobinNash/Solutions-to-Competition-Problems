# Lucky Number #
# July 4, 2021 #
# By Robin Nash #

for test in range(int(input())):
    n = int(input())
    total = 0

    n = str(n)
    while len(n) > 1:
        n = sum(map(int,n))
        n = str(n)

    print(n)
