#david punchak
#Lab #3 B Take home
#SE126
#1/24/24

#This is the voter project that was given to us in python 1 but not is is reading a csv file to be able to get the information

#-----------Outputs
#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed


#------------var dictnary-------------
#numberList = the numbers of the person
#AgeList = the ages of the people
#regesteredList = the people that are regestered
#votedList = the people that voted

#NoElgAndReg = people that are not over the age of 18
#overAgeNotReg = the total of people that are over age but did not reg
#canVoteDidNot = total of people that can vote but did not
#DidVote = the total number of people that voted
#total_recoreds = the total number of recoreds


#-----------Start of main code---------------


#this is importing the csv file
import csv


#setting up the lists
numberList = []
AgeList = []
regesteredList = []
votedList = []


#this is just setting the varables for the number of voters
NoElgAndReg = 0
overAgeNotReg = 0
canVoteDidNot = 0
didVote = 0
total_recoreds = 0

#this is just opening the text file
with open("Labs/TextFiles/voters_202040.csv") as csvFile:

    #this is readign the csv and setting it to file
    file = csv.reader(csvFile)

    #for every recored in the file it would add the respectiive rec to that list
    for rec in file:
        numberList.append(int(rec[0]))
        AgeList.append(rec[1])
        regesteredList.append(rec[2])
        votedList.append(rec[3])
        #print(f"Test {AgeList}")
        total_recoreds += 1


#-------------this is where is gets complex-----------------
        
#for every entrey in age list its seeing if they are over 18 of not adding one
for index in range(0, len(AgeList)):
    if int(AgeList[index]) >= 18:
        if regesteredList[index] == "N":
            #this is if they are regestered they move on to the next step if not than its adding one
            overAgeNotReg += 1
        else:
            if votedList[index] == "Y":
                #this is if the person has voted and if they are regestered to vote it adds it to one, if not than they did not vote
                didVote += 1
            else:
                canVoteDidNot += 1
    else:
        NoElgAndReg += 1

#this is just printing the final outputs.
print(f"There are {NoElgAndReg} people not eligible to register (Under 18).")
print(f"There are {overAgeNotReg} people over 18 but not registered.")
print(f"There are {canVoteDidNot} people that can vote but did not.")
print(f"There are {didVote} people that voteded.")
print(f"There was a total of {total_recoreds} people.")