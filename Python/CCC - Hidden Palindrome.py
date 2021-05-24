# Hidden Palindrome #
# November 18, 2018
# By Robin Nash

word = [i for i in input()]

palindromes = []

for loop in range(2):
    for i in range(1,len(word)+1):
        if loop == 0:
            letters = 1
            for ii in range(1,len(word)):
                try:
                    if word[i-ii] == word[i+ii]:
                        letters += 2
                    else:
                        palindromes.append(letters)
                        break
                except IndexError:
                    palindromes.append(letters)
                    break
        else:
            letters = 0
            for ii in range(len(word)):
                try:
                    if word[i-ii] == word[i+ii+1]:
                        letters += 2
                    else:
                        palindromes.append(letters)
                        break
                except IndexError:
                    palindromes.append(letters)
                    break
if max(palindromes) == 0:
    print(1)
else:
    print(max(palindromes))
        
    
    
#1542567278.0