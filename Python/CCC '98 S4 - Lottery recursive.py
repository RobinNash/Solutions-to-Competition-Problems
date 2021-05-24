# Lottery # 
# December 29, 2020
# By Robin Nash
# Recursive Solution

def addBrackets(line, close = 0, X = True):
    '''adds brackets to terms where they need to be'''
    
    # if we've reached the front, add opening brackets if necessary
    if len(line) == 1:
        return ["("*close+line[0]]

    # If we're bracketing multiplication and the proceeding
    # operator isn't X, the brackets must be closed
    if X and line[-2] != "X":
        line[-1] = "("*close + line[-1]
        close = 0
        
    # Add a closing bracket to each term
    else:
        line[-1] += ")"
        close += 1
        
    return addBrackets(line[:-2], close, X) + line[-2:]

def glueTerms(line):
    '''takes a list and groups each expression in brackets into one term
    ex. ['(1', 'X', '1)', '+', '1'] -> ['(1 X 1)', '+', '1']'''
    if len(line) == 0:
        return []
    
    # get index of last item in group
    i = line[0].count("(")*2 + 1

    return [" ".join(line[:i])] + glueTerms(line[i:])

tests = int(input())
for test in range(tests):
    
    line = input().split()
    
    # group multiplication
    line = addBrackets(line,0,True)
    line = glueTerms(line)
    
    # add the rest of the brackets for +/-
    line = addBrackets(line,0,False)
    line = glueTerms(line)[0]
    
    #shed the extra brackets on the ends
    print(line[1:-1])
    print() # problem asks for newline after each


'''
Do X first, then +/-

ex   1 + 1 + 1 X 1 X 1 + 1 X 1
is   1 + 1 + ((1 X 1) X 1) + (1 X 1) -> 1 + 1 + n + m
then ((1 + 1) + ((1 X 1) X 1)) + (1 X 1) -> ((1 + 1) + n) + m

ex 1 X 1 X 1 X 1
is (((1 X 1) X 1) X 1)

start at the end and go backwards

if nothing comes before n:
    add (*close to n
if X comes before n: add ) to n and close += 1
else:
    add (*close to n and close = 0

- then take the list and group what's in the brackets so they each act as
one term (ex ['(1','X','1)','+','1'] -> ['(1 X 1)','+','1'])

then group the way you did with multiplication but easier
'''


