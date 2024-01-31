#david punchak




#making a long and lat project 
#giving a location that would be given a random 4 and the user has to guess. 




#---------------------------------------------------------------------------

import random
import csv

location = []
long = []
lat = []

randDeside = 0



randDeside = random.randint(0, 41)

print(randDeside)

with open("SE126/MidTermProject/TextFile/locations.csv") as csvFile:

    file = csv.reader(csvFile)

    
    for rec in file:
        
        location.append(str(rec[0]))
        long.append(float(rec[1]))
        lat.append(float(rec[2]))

        print("he")
        





print(f"What is the long and lat of {location[randDeside]} ")


