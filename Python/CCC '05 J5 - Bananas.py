#Bananas
# October 24, 2020
# By Robin Nash

def isMonkey(s,S,monkey):
    if s == "":
        return True if not S and monkey else False
    elif s[0] == 'N':
        return False if not monkey else isMonkey(s[1:],S,False)
    elif s[0] == 'B':
        return False if monkey else isMonkey(s[1:],S+1,False)
    elif s[0] == 'S':
        if not S:
            return False
        return False if not monkey else isMonkey(s[1:],S-1,True)
    elif s[0] == 'A':
        return False if monkey else isMonkey(s[1:],S,True)
    else:
        return False

while True:
    s = input()
    if s == "X":
        break
    if s:
        print("YES" if isMonkey(s,0,False) else "NO")
    else:
        print("NO")
####s = input()
### yes: "A","ANA","ANANA","BANANAS","BASNBAS","BASNA", "BAS", "BBBASSS", "BANANASNBANANAS"
### no: "", "BS", "ABSA","BANANA","BANSA","ANABANANAS","BANASSNBBANAS","ANAANA","AN","BANS"
##for s in [ "A","ANA","ANANA","BANANAS","BASNBAS","BASNA", "BAS", "BBBASSS", "BANANASNBANANAS","", "BS", "ABSA","BANANA","BANSA","ANABANANAS","BANASSNBBANAS","ANAANA","AN","BANS"]:
##    if s:
##        print("YES" if isMonkey(s,0,False) else "NO",s)
##    else:
##        print("NO",s)
#1603503750.3834548