# Lottery #
# January 7, 2020
# By Robin Nash

for t in range(int(input())):
    line = input().split()

    while "X" in line:
        if len(line) == 3:
            break
        x = line.index("X")
        new = "("+line[x-1]+" X "+line[x+1]+")"
        del line[x:x+2]
        line[x-1] = new

    while len(line) > 3:
        new = "("+" ".join(line[:3])+")"
        del line[:2]
        line[0] = new

    print(" ".join(line))
    print()



# sample inputs and their respective outputs
'''
8
1234 + 4567
1234 + 4567 X 11
12 X 34 + 56 X 78 + 90
12345 + 56789 X 34567 - 87654
12 - 34 X 56 X 78
1 X 2 X 3 X 4 X 5 X 6 X 7 X 8 X 9
12 - 23 X 34 X 45 X 56 + 67 X 78 X 89 - 90
476 X 983 + 906 X 9182 - 2735 X 125
'''

'''
1234 + 4567

1234 + (4567 X 11)

((12 X 34) + (56 X 78)) + 90

(12345 + (56789 X 34567)) - 87654

12 - ((34 X 56) X 78)

(((((((1 X 2) X 3) X 4) X 5) X 6) X 7) X 8) X 9

((12 - (((23 X 34) X 45) X 56)) + ((67 X 78) X 89)) - 90

((476 X 983) + (906 X 9182)) - (2735 X 125)
'''
#1578436684.0
