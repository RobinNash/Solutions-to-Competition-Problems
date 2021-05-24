# Fix #
# October 21, 2018
# By Robin Nash
def fix(lines):
    for i in range (3):
        line = lines[i]
        for ii in range(3):
            if ii!=i:
                if lines[ii][:len(line)] == line or lines[ii][-len(line):] == line:
                    return(True)
N = int(input())
for verses in range(N):
    lines = []
    for i in range(3):
        line = input()
        lines.append(line)
    if fix(lines):
        print("No")
    else:
        print("Yes")

        
#1540162208.0