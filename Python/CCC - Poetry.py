# Poetry #
# October 20, 2018
# By Robin Nash

def lastSyllable(line):
    word = line.split(" ")[-1]
    for i in range(len(word)):
        if vowels.count(word[-i]):
            word = (word[-i:])
            break
    return(word)

vowels = "aeiou"

rhymes=[]
N = int(input())
for i in range(N):
    syllables=[]
    for ii in range(4):
        line = input()
        line = line.lower()
        syllables.append(lastSyllable(line))
        
    if syllables[0] == syllables[1] == syllables[2] == syllables[3]:
        rhymes.append("perfect")
    elif syllables[0] == syllables[1] and syllables[2] == syllables[3]:
        rhymes.append("even")
    elif syllables[0] == syllables[2] and syllables[1] == syllables[3]:
        rhymes.append("cross")
    elif syllables[0] == syllables[3] and syllables[2] == syllables[1]:
        rhymes.append("shell")
    else:
        rhymes.append("free")

for rhyme in rhymes:
    print(rhyme)
# Test 4

'''
a monkey
a toy
a key
an alloy
a c
a c
I c
I c
c
x
x
c
azzzzzzzzz
''''''
free
perfect
shell
even
perfect
'''
        
        
    
#1540069724.0