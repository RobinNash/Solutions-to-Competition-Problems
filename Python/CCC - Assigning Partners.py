# Assigning Partners #
# November 18, 2018
# By Robin Nash

students = int(input())

line1 = input().split(" ")
line2 = input().split(" ")

pairing = "good"
for i in range(students):
    if line1[i] == line2[i]:
        pairing = "bad"
        break
    if sorted([line1[i], line2[i]]) != sorted([line2[line2.index(line1[i])],line1[line2.index(line1[i])]]):
        pairing = "bad"
        break
print(pairing)
#1542564646.0