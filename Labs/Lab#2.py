#David punchak
#SE126 
#january/17/24


#The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event.

#Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list.

#After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#--------------Var dictnary----------------
#room = this is the room that being looked at
#maxpeople = this is the max amount of people that can fit in a room
#going = this is the amount of people going
#roomTotal = this is the math for getting the amount of people if its over or under the max
#loopTime = this is the amount of times that the list has run
#overPop = this is the list for the roos over the population
#underPop = this is the list for the rooms under the popuation
#overRoom = this is the list fot the room that is over
#roomMax = this is the list for the max amount of people
#attending = this is the list for people going
#---------------functions/imports-----------------
import csv #this is just the csv file that is being added
#-----------start of the main code------------------
room = 0
maxPeople = 0
going = 0
roomTotal = 0
loopTime = 0
#this is setting the list for the code
overPop = []
underPop = []
overRoom = []
roomMax = []
attending = []
#Welcoming the user and having the deceraton for the intro
print("Room\t\t\t Max people.    People going. \t How much over.\n------------------------------------------------------")
#this is having the lab file opened
with open("SE126\Labs\TextFiles\lab2a.csv") as csvfile:
    
    #setting file to be able to read each rec in the file
    file = csv.reader(csvfile)

    for rec in file:
        #start of the for loop for each rec in the file
        #Need to have the math here

        room = rec[0]
        maxPeople = int(rec[1])
        going = float(rec[2])
        loopTime += 1
        roomTotal = maxPeople - going
        
        #print(f"This is loop {loopTime}")#take out
        #print(roomTotal)#take out

        #if the number we get from the math is under 0 it will add it to a list if it is over 0 it will add it to a different list
        if roomTotal >= 0:
            #adding it to the list that is over 0
            #this is very pointless but it is just here to be here
            overPop.append(roomTotal)
        else:
            #adding the name of the room and the amount of people that it is over by in the list
            underPop.append(roomTotal)
            overRoom.append(room)
            roomMax.append(maxPeople)   
            attending.append(going)         
#this is to have the correct room print and where it is located in the list by index
index = -0
numberOfTimes = 0
for i in overRoom:
    underPop[index] = underPop[index] * -1
    #print(f"The room {overRoom[index]} is {underPop[index]} over the max amount of people")
    print(f"{overRoom[index]:20} \t{roomMax[index]:5} \t\t{attending[index]:10}  \t\t{underPop[index]} ")
    index += 1
    numberOfTimes += 1

print(f"\nThere were {loopTime} rooms that we tested.")
print(f"You have {numberOfTimes} rooms that are over")



input("Press -Enter- to end......")

#End of the with loop and the for loops