# Attack of the CipherTexts #
# November 25, 2018
# By Robin Nash

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input()
code = input()
decipher = input()

cipher = [[text[i],code[i]] for i in range(len(code))]
cipher.extend([[".",ch] for ch in ALPHA if ch not in code])

for ch in decipher:
    print(cipher[[i[1] for i in cipher].index(ch)][0],end='')
    
#1543176320.0