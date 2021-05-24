# Signage #
# December 15, 2018
# By Robin Nash

def getLine(x, line, chars):
    if len(line)>1:
        spaces = len(line)-1
        periods = x-chars
        evenSpaces = [periods//spaces for i in range(spaces)]
        extraSpaces = periods % spaces
        
        for i in range(extraSpaces):
            evenSpaces[i]+=1
        for i in line[:-1]:
            line.insert(line.index(i)+1, '.'*evenSpaces.pop(0))
    elif len(line) == 1:
        line+=['.'*(x-len(line[0]))]

    return line


    
x = int(input())

message = 'WELCOME TO CCC GOOD LUCK TODAY'.split(' ')

while message != []:
    chars = 0
    for i in range(len(message)):
        if chars+len(message[i])+i <= x:
            chars+=len(message[i])
            words = i+1
        else:
            break
    if message != []:
        line = getLine(x, [message.pop(0) for i in range(words)], chars)
        
        for part in line:
            print(part,end='')
        print()

##for x in [i for i in range(7,40)]+[70]:
##    message = 'WELCOME TO CCC GOOD LUCK TODAY'.split(' ')
##    for yeet in range(2):
##        chars = 0
##        for i in range(len(message)):
##            if chars+len(message[i])+i <= x:
##                chars+=len(message[i])
##                words = i+1
##            else:
##                break
##        if message != []:
##            line = getLine(x, [message.pop(0) for i in range(words)], chars)
##        else:
##            line = getLine(x, message,chars)
##
##        for part in line:
##            print(part,end='')
##        print()





        
#1544842424.0