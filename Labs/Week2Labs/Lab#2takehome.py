#David punchak
#SE126 
#1/18/24


#This project is reading a csv file and getting the output based on the information in the file

#importing the csv file
import csv


#just a total counter
total = 0

#printing a welcome to the user
print("Type\t Brand\t\tCPU\tRam\t1 Disk\tHHD?\t2 Disk\t Os\tYear")
print("-------------------------------------------------------------------------------")

#this is opening the text file, depending on how this is sent to you it might brake here because i dont know where you keep the file 
with open("SE126\Labs\TextFiles\lab2b.csv") as csvFile:

    #this is reading the csv file and making it set to file
    file = csv.reader(csvFile)

    #this is the loop for every recored in the file
    for rec in file:

        #this is if the computer is a desktop of if its a laptop
        if rec[0] == "D":
            comp_type = "DeskTop"
        elif rec[0] == "L":
            comp_type = "LapTop"
        else:
            comp_type = "-Error-"

        #this is for if the computer is a dell, hp, or gateway
        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "GateWay"
        elif rec[1] == "HP":
            manu = "HP"
        else:
            manu = "-Error-"


        #this is just setting the recored for the information that we have. if you were to get ride of one of the lines of information it would get brake. 
        pross = rec[2]
        ram = rec[3]
        size = rec[4]

        #class note / KT help
        #if rec[5] == 2 than we make rec6 to the one down the line rec[8] would be year, else rec5 would be blank is os and rec [7] is year

        #this is the way we get to see if the information is not there than we just move on.
        if rec[5] == "2":
            drive = rec[5]
            hd2 = rec[6]
            os = rec[7]
            year = rec[8]
        else:
            drive = rec[5]
            hd2 = "---"
            os = rec[6]
            year = rec[7]

        #this is just printing out the final information for the user to read 
        print(f"{comp_type:4}\t {manu:7}\t {pross:2}\t {ram:2}\t {size:5}\t {drive:5}\t {hd2:5}\t {os:5}\t {year:5}")
        #just a counter for how many recoreds are in this list
        total += 1

#printing out the final good bye to the user
print(f"\nThere were {total} computers.")
input("--------------------------Enter To Quit-------------------------------------")
        