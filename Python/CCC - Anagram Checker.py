# Anagram Checker #
# November 24, 2018
# By Robin Nash

text1 = [i for i in input() if i != " "]
text2 = [i for i in input() if i != " "]

anagram = True

for ch in text1:
    if text1.count(ch) != text2.count(ch) or len(text1) != len(text2):
        anagram = False
        print("Is not an anagram.")
        break

if anagram:
    print("Is an anagram.")

#1543081054.0