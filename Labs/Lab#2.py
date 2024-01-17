#David punchak
#SE126 
#january/17/24


#The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event.

#Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list.

#After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#--------------Var dictnary----------------




#---------------functions/imports-----------------
import csv


#-----------start of the main code------------------
room = 0
maxPeople = 0
going = 0
roomTotal = 0
loopTime = 0#take out


overPop = []
underPop = []
overRoom = []
roomMax = []
attending = []

print("Room\t\t\t Max people.    People going. \t How much over.\n------------------------------------------------------")
#this is having the lab file opened
with open("Labs/TextFiles/lab2a.csv") as csvfile:
    
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
            overPop.append(roomTotal)
        else:
            #adding the name of the room and the amount of people that it is over by in the list
            underPop.append(roomTotal)
            overRoom.append(room)
            roomMax.append(maxPeople)   
            attending.append(going)         
                        
#this is printing out the rooms amount of rooms tested


#this is to have the correct room print and where it is located in the varable
index = -1
numberOfTimes = 0
for i in overRoom:
    index += 1
    underPop[index] = underPop[index] * -1
    #print(f"The room {overRoom[index]} is {underPop[index]} over the max amount of people")
    print(f"{overRoom[index]:20} \t{roomMax[index]:5} \t\t{attending[index]:10}  \t\t{underPop[index]} ")
    numberOfTimes += 1

print(f"\nThere were {loopTime} rooms that we tested.")
print(f"You have {numberOfTimes} rooms that are over")



input("Press -Enter- to end......")

#End of the with loop and the for loops