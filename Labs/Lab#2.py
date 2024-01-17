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




#this is having the lab file opened
with open("Labs/TextFiles/lab2a.csv") as csvfile:
    
    #setting file to be able to read each rec in the file
    file = csv.reader(csvfile)

    for rec in file:
        #start of the for loop for each rec in the file
        #Need to have the math here
        room = rec[0]
        maxPeople = rec[1]
        going = rec[2]

        roomTotal = maxPeople - going

        print(roomTotal)




#End of the with loop