# Multiple Choice #
# December 09, 2018
# By Robin Nash

questions = int(input())

studentAnswers = [input() for i in range(questions)]
correctAnswers = [input() for i in range(questions)]

print(len([i for i in range(questions) if studentAnswers[i] == correctAnswers[i]]))
#1544393724.0