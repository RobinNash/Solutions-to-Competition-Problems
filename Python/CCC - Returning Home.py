# Returning Home
# November 17, 2018
# By Robin Nash

turns = []
streets = []

direction = input()
while direction != "SCHOOL":
    if direction == "R":
        turns.append("LEFT")
    elif direction == "L":
        turns.append("RIGHT")
    else:
        streets.append(direction)
    direction = input()

turns.reverse()
lastTurn = turns.pop()
streets.reverse()

for i in range(len(streets)):
    print("Turn",turns[i],"onto",streets[i],"street.")
print("Turn",lastTurn,"into your HOME.")

    
    
#1542487850.0