# From 1987 to 2013 #
# November 18, 2018
# By Robin Nash

year =int(input())

while True:
    year+=1
    cont = False
    for i in str(year):
        if str(year).count(i) > 1:
            cont = True
            break
    if cont:
        continue
    break
print(year)
#1542561512.0