#david punchak
#january 30 - feb 
#MidTerm Project
#SE126.10



#making a long and lat project 
#giving a location that would be given a random 4 and the user has to guess. 
#

#------------Example----------
#What is the location of hover dam

#long lat 1
#long lat 2
#long lat 3
#long lat 4

#what do you think it is: 

#wrong - take one life away, move to next long and lat
#correct - Add one point, move to next long and lat.

#---------------------------------------------------------------





#--------------------------------Main code------------------------------------------

import random
import csv

location = []
long = []
lat = []

randDeside = 0

randDeside2 = 0
randDeside3 = 0
randDeside4 = 0


randDeside = random.randint(0, 41)

randDeside2 = random.randint(0, 41)
randDeside3 = random.randint(0, 41)
randDeside4 = random.randint(0, 41)

#print("Before")
#print(randDeside)

with open("SE126/MidTermProject/TextFile/locations.txt", encoding = "utf-8") as csvFile:

    file = csv.reader(csvFile)

    for rec in file:
        location.append(rec[0])
        long.append(float(rec[1]))
        lat.append(float(rec[2]))


print(f"What is the Long and lat of location {location[randDeside]}")

print(f"\nA: long {long[randDeside]} Lat {lat[randDeside]} ")

print(f"B: long {long[randDeside2]:.2f} Lat: {lat[randDeside2]} ")
print(f"C: long {long[randDeside3]:.2f} Lat: {lat[randDeside3]} ")
print(f"D: long {long[randDeside4]:.2f} Lat: {lat[randDeside4]} ")

userAnw = input("\nWhat is your answer: ")
