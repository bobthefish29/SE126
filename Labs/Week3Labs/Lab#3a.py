#david punchak
#Se126
#LAb #3 A

# this is the same thing as lab #2 a but it has a differance at prints. The Code is mostly going to be the same as the first example but there will be a difference when it coes to the out pust.

#The way the information is going to be sourted will be the same

#Need to find the computers and the laptops that are older than 2016 and display the price of all the computers.



#-------------A lot of this code is just taken from both the lab#2 take home lab and from the week 3 day 1 demo.------------ 



#-----------------Var dictonary-----------------
#total_counter = this is just a total count of the recoreds
#desktop_count = this is the amout of desktops that are there
#laptop_count = THis is the count for how many laptops are there
#DTValue = This is just the value of all the desktops
#LTValue = This is the total of the laptops
#totalValue = this is just the total value of all the computers and laptops



#--------------------Main code------------------------

#this is importing the csv files
import csv


#this is just setting up the var for them to be able to run in the program.
total_counter = 0
desktop_count = 0
laptop_count = 0
DTValue = 0
LTValue = 0

#this is setting up the lists so that when i call them in the program they are there.
comp_type_list = []
manu_list = []
processor_list =[]
ram_list =[]
size_list = []
drive_list = []
hd2_list =[]
os_list = []
year_list = []

#Just some information to make it looke better when printed
print(f"comp type\t Manu   \tCPU \tRam\t Size\t Drive\t HD2\t OS\t Year")
print("-----------------------------------------------------------------------------------------------------------")


#this is opening the textfile so the information could be read. This is mostlikly the thing that will breake becasue every time it does.
with open("Labs/TextFiles/lab3a.csv") as csvFile:


    #this is reading the text file and seeting the information to file
    file = csv.reader(csvFile)


    #reading every recored in the filed and doing the calulations to see if its able to be sorted.
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

        #this what is being able to tell if the the information in rec 2 is able to be prossesed or if it would get skiped
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

        #Just a testing print test to see if the information would be sorted into there groups.    
        #print(f"{comp_type:4}\t {manu:7}\t {pross:2}\t {ram:2}\t {size:5}\t {drive:5}\t {hd2:5}\t {os:5}\t {year:5}")

        total_counter += 1

        #this is setting the different information to there respective lists.
        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processor_list.append(pross)
        ram_list.append(ram)
        size_list.append(size)
        drive_list.append(drive)
        hd2_list.append(hd2)
        os_list.append(os)
        year_list.append(year)
#out of loop


#For every entrey in the list it would print the output
for index in range(0, total_counter):
    print(f"{comp_type_list[index]:9}\t {manu_list[index]:7}\t {processor_list[index]:2}\t {ram_list[index]:2}\t {size_list[index]:5}\t {drive_list[index]:5}\t {hd2_list[index]:5}\t {os_list[index]:5}\t {year_list[index]:5}")


#this is how we are able to tell if the computer is a desktop of if its a laptop. It also has if its older than 2016 
for index in range(0, total_counter):
    if comp_type_list[index] == "DeskTop" and int(year_list[index]) <= 16:
        desktop_count += 1
    elif comp_type_list[index == "LapTop"] and int(year_list[index]) <= 16:
        laptop_count += 1


#this is just the math to be able to count total value of the computers and stuff.
DTValue = desktop_count * 2000
LTValue = laptop_count * 1500
totalValue = LTValue + DTValue

#this is just printing the final outputs to the user
print("-------------------------------------------------------")
print(f"You have {desktop_count} Desktops. It would cost ${DTValue:.2f} to replace.")
print(f"You have {laptop_count} LapTops. It would cost ${LTValue:.2f} to replace.")
print(f"In total it would cost ${totalValue} to replace all.")

#this is to keep the user in the program so they could see the information that is being given and not have it close.
input("\n--------Press Enter To close-----------")

