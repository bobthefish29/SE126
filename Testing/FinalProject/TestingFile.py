f = open("Testing/FinalProject/TextFiles\Maze.csv", "rt")

import csv



score = []
userName = []
width = []
height = []
    
totalList = []

#print(f)
#print(f.read())
#input("\n\n\nTesting")

for x in f:
    score.append([0])
    userName.append([1])
    width.append([2])
    height.append([3])
    
    totalList.append([score[x],[1],int([2]),int([3])])

print(totalList)
input("\n\n\nTesting")

with open("Testing/FinalProject/TextFiles/Maze.csv", "rt") as csvFile:
    file = csv.reader(csvFile)
    for rec in file:
        
        score.append(rec[0])
        userName.append(rec[1])
        width.append(rec[2])
        height.append(rec[3])
    
        totalList.append([int(rec[0]),rec[1],int(rec[2]),int(rec[3])])

print(totalList)