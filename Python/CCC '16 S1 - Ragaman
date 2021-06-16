# CCC '16 S1 - Ragaman #
# June 15, 2021
# By Robin Nash

a = input()
b = input()

asterisks = b.count("*")
anagram = True
checked = ''
for c in a:
    if c not in checked:
        checked += c
        
        dist = a.count(c) - b.count(c)
        asterisks -= dist
        
        if dist < 0 or asterisks < 0:
            anagram = False
            break

print("A" if anagram else "N")
