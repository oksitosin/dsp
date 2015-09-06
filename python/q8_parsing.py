#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv

fb = csv.reader(open("football.csv", "rb"))
goals = []
goals_allowed=[]
team=[]

for data in fb:
    goals.append(data[5])
    goals_allowed.append(data[6])
    team.append(data[0])
    
del goals[0]
del goals_allowed[0]
del team[0]    

goals=map(int,goals)
goals_allowed=map(int,goals_allowed)

dif= [a - b for a, b in zip(goals, goals_allowed)]

comb=zip(dif,team)
comb.sort()

print comb[0]

