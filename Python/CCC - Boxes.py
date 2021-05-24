# Boxes #
# November 19, 2018
# By Robin Nash

boxes = []
for i in range(int(input())):
    boxes.append([int(i) for i in input().split(" ")])

for i in range(int(input())):
    item =[int(i) for i in input().split(" ")]
    goodBoxes = []
    for box in boxes:
        good = True
        for i in range(3):
            if sorted(item)[i]>sorted(box)[i]:
                good = False
        if good:
            goodBoxes.append(box[0]*box[1]*box[2])
    if goodBoxes != []:
        print(min(goodBoxes))
    else:
        print("Item does not fit.")
#1542596672.0