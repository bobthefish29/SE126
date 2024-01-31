#David punchak 
#sE126 int- mid python
#1/31/2024
#Lab#4 take home




#------------------Task for the lab------------------------------------------
#this Process the lists to print the them as they appear in the file

#Re-process the lists to add the House Motto (dependent on Field4/Allegiance; see motto chart below)

#Re-Process the lists to print each record fully with the House Mottos

#Re-process the lists to find the average age within the list, then

#Print the total number of people in the list

#Print the average age - rounded to a whole number {:.0f}

#Print tallies/final counts for each allegiance (Field4)
#---------------------------------------------------------------------------


#This project was fun to do.
#



#-----------------------Starting of main code---------------------------

import csv


#Setting the lists and the var's

#this is for the list's that i made
fName = []
lName = []
age = []
nicName = []
house = []
houseMotto = []

#this is for the math to find the avg age
avgAge = 0
total_rec = 0
ageMath = 0

#They are the var's for getting the counting for the amout of people in that house.
houseS = 0 #house stark
houseT = 0 #house Tully
houseL = 0 #house Lanister
nightW = 0 #night watch (Favort family )
houseB = 0 #house brathion (i dont rember this one)
houseTr = 0 #house targien (Mother of dragon family)

#just a basic display for the user
print("First Name   |\t Last Name    |  age \t   Nic name \t\t House ")
print("---------------------------------------------------------------------------------------------------------")

#oppening the file
with open("SE126\Labs\TextFiles\lab4A_GOT_NEW.txt") as csvFile:
    #reading the file as a csv file
    file = csv.reader(csvFile)

    #for each recored in the file it is going to loop this
    for rec in file:
        #this is adding the item to the respected list
        fName.append(str(rec[0]))
        lName.append(str(rec[1]))
        #casting it as a float so it can be done with math
        age.append(float(rec[2]))
        nicName.append(str(rec[3]))
        house.append(str(rec[4]))

        #What i am thinking is if i do it like, if house at rec == night watch than it would append the motto to that rec i might need to make a 2d list than read that

        #i did not end up doing that, i just did it based on if it was there at rec 4 and was the name it would be called that, It could break because the else at the end is not for an error but it is just the last house.
        if rec[4] == "House Stark":
            houseMotto.append("Winter is Comming")
            #adding the tallie for the house member and it is repeated
            houseS += 1

        elif rec[4] == "House Baratheon":
            houseMotto.append("Ours is the fury")
            houseB += 1

        elif rec[4] == "House Tully":
            houseMotto.append("Family. Duty. Honor")
            houseT += 1

        elif rec[4] == "Night's Watch":
            houseMotto.append("And now my watch begins")
            nightW += 1

        elif rec[4] == "House Lannister":
            houseMotto.append("Hear me roar!")
            houseL += 1

        else:
            houseMotto.append("Fire & Blood")
            houseTr += 1



        #the total number of recoreds
        total_rec += 1



#this is just printing the first bit of data, this is just repeating the list but in a nice way for the user
for i in range(0, len(fName)):
    print(f"{fName[i]:8}     |    {lName[i]:10}  |  {age[i]:4.0f}\t   {nicName[i]:15}\t {house[i]:9}")
print("------------------------------------------------------------------------------------------------------------------\n")

#this is also just printing the list for the user, but this one has the house motto for the user to see
print("First Name   |\t Last Name    |  age \t   Nic name \t\t House \t\t\t House Motto ")
print("\n---------------------------------------------------------------------------------------------------------")
for i in range(0, len(fName)):
    print(f"{fName[i]:8}     |    {lName[i]:10}  |  {age[i]:4.0f}\t   {nicName[i]:15}\t {house[i]:16} \t {houseMotto[i]} ")
print("-----------------------------------------------------------------------------------------------------------------------\n")

#this is doign the math for the age, it is adding the value of age at that index point to a total counter
for i in range(0, len(age)):
    ageMath = ageMath + age[i]
#this is taking the total that was found before it and dividing it by the total number of people
avgAge = ageMath / total_rec

#this is just the printing for the user at the end with how mant rec, the avg age and the tallies for the house members. 
print(f"There are {total_rec} people in the list. The average age is {avgAge:.0f}.\n")
print(f"House Stark - {houseS}\nHouse Barathon - {houseB}\nHouse Tully - {houseT}\nNight's Watch - {nightW}\nHouse Lannister - {houseL}\nHouse Targaryen - {houseTr}\n")

#Input just so it wont close on the user.
input("-------------------------------------Press Enter To Quit----------------------------------------------------")