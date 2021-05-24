# Canadian Calorie Counting #
# November 17, 2018
# By Robin Nash

calories = 0
for i in range(4):
    choice = int(input())-1
    calories+=[[461,431,420,0],[100,57,70,0],[130,160,118,0],[167,266,75,0]][i][choice]
print("Your total Calorie count is ",calories,".",sep='')
    
#1542488326.0