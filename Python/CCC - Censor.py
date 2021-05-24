# Censor #
# November 29, 2018
# By Robin Nash

for i in range(int(input())):
    line = input().split(" ")
    line.append("")
    for word in line:
        if len(word) == 4:
            word = "****"
        if word == '':
            print(word)
            break
        print(word,end=" ")
#1543509044.0