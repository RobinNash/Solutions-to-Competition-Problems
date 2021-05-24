# TopYodeller #
# October 21, 2018
# By Robin Nash

class Yodeller:
    def __init__(self,contestantNum,allRounds):
        self.contestant = contestantNum+1
        self.allRounds = allRounds
        
    def worstRank(self):
        ranks = []
        for round in self.allRounds:
            score = round[self.contestant-1]
            for i in range(len(round)):
                if score == (sorted(round,reverse=True))[i]:
                    ranks.append(i+1)
                    break
        return(sorted(ranks, reverse = True)[0])

    def score(self):
        score = self.allRounds[-1][self.contestant-1]
        return(score)          

nk = input()
yodellersNum,rounds = int(nk.split(" ")[0]),int(nk.split(" ")[1])
allRounds = []
for i in range(rounds):
    round = input()
    allRounds.append(round.split(" "))
    for ii in range(len(round.split(" "))):
        allRounds[i][ii] = int(allRounds[i][ii])
        if i > 0:
            allRounds[i][ii]+=allRounds[i-1][ii]
    
yodellers = []
for i in range(yodellersNum):
    yodeller = Yodeller(i,allRounds)
    yodellers.append(yodeller)

for i in range(yodellersNum):
    try:
        topYodeller=sorted(yodellers, key=lambda yodeller: yodeller.score(), reverse = True)[i]
        print("Yodeller ",topYodeller.contestant," is the TopYodeller: score ",topYodeller.score(),", worst rank ",topYodeller.worstRank(),sep="")
        if sorted(yodellers, key=lambda yodeller: yodeller.score(), reverse = True)[i+1].score() != topYodeller.score():
            break
    except IndexError:
        break



    

#1540149504.0