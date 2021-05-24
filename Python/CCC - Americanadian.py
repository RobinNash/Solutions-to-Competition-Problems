# Americanadian
# October 20, 2018
# By Robin Nash

consonants = "bcdfghjklmnpqrstvwxz"

words = []
while True:
    word = input()
    if word!="quit!":
        words.append(word)
    else:
        break

for word in words:
    if len(word) > 4:
        if consonants.count(word[-3]):
            if word[-2:] == "or":
                word=word.replace(word[-2:],"our")
    print(word)
    
#1540004492.0