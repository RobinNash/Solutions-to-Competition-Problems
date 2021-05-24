# Trident #
# October 20, 2018
# By Robin Nash
t = int(input())
s = int(input())
h = int(input())

for i in range(t):
    print("*"," "*s,"*"," "*s,"*",sep="")
print("*"*(3+2*s))

for i in range(h):
    print(" "*s,"*")
#1540006738.0