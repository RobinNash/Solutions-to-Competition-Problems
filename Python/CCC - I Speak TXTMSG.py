# I Speak TXTMSG
# November 17, 2018
# By Robin Nash

abbreviations = ['CU', ':-)', ':-(', ';-)', ':-P', '(~.~)', 'TA', 'CCC', 'CUZ', 'TY', 'YW', 'TTYL']
translations = ['see you', "I'm happy", "I'm unhappy", 'wink', 'stick out my tongue', 'sleepy', 'totally awesome', 'Canadian Computing Competition', 'because', 'thank-you', "you're welcome", 'talk to you later']

word = input()
while word != "TTYL":
    if word in abbreviations:
        print(translations[abbreviations.index(word)])
    else:
        print(word)
    word = input()

print(translations[-1])
#1542490066.0