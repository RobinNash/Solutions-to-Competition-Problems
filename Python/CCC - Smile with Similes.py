# Smile with Similes
# October 20, 2018
# By Robin Nash

n = int(input())
m = int(input())

adjs = []
nouns = []
for i in range(n):
    adj = input()
    adjs.append(adj)
for i in range(m):
    noun = input()
    nouns.append(noun)

for adj in adjs:
    for noun in nouns:
        print(adj,"as",noun)
    
#1540014914.0