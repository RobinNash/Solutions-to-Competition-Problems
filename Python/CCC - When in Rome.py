# When in Rome #
# October 29, 2018
# By Robin Nash

def getSum(equation):
    for subtraction in subtractions:
        if subtraction[0] in equation:
            equation = equation.replace(subtraction[0],str(subtraction[1])+" ")

    for addition in additions:
        if addition[0] in equation:
            equation = equation.replace(addition[0],str(addition[1])+" ")

    equation = equation.replace("+","")
    equation = equation[:-2].split(" ")
    equation = [int(i) for i in equation]

    return sum(equation)

additions = [["I",1],["V",5],["X",10],["L",50],["C",100],["D",500],["M",1000]]
subtractions = [["IV",4],["IX",9],["XL",40],["XC",90],["CD",400],["CM",900]]

allNumerals = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100],\
            ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5],\
               ['IV', 4], ['I', 1]]

for i in range(int(input())):
    equation = input()

    number = getSum(equation)

    numerals = ""
    if number <= 1000:
        for numeral in allNumerals:
            for i in range(number//numeral[1]):
                numerals+=numeral[0]
            number%=numeral[1]
    else:
        numerals = "CONCORDIA CUM VERITATE"
    print(equation+numerals)
#1540771246.0