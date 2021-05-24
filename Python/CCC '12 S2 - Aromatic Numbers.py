# Aromatic Numbers #
# August 02, 2019
# By Robin Nash


line = input()


bases = "IVXLCDM"
roman = {}
for i in range(7):
    roman[bases[i]] = [1,5,10,50,100,500,1000][i]

pairs = [line[i:i+2] for i in range(0,len(line)-1,2)]


total = 0
for i in range(len(pairs)):
    try:
        if roman[pairs[i+1][1]] > roman[pairs[i][1]]:
            total -= int(pairs[i][0])*roman[pairs[i][1]]
        else:
            total += int(pairs[i][0])*roman[pairs[i][1]]
    except IndexError:
        total += int(pairs[i][0])*roman[pairs[i][1]]
    
print(total)
#1564714074.0