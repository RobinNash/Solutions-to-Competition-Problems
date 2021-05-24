# Rotating Letters #
# November 18, 2018
# By Robin Nash

ROTATEABLES= 'I, O, S, H, Z, X, N'.split(", ")

rotate = "YES"
for i in input():
    if i not in ROTATEABLES:
        rotate = "NO"
        break
print(rotate)
#1542561858.0