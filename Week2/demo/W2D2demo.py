#text file opening review + 1d list

#this is getting the import of the csv file and it is havng it read every thing in the fle
import csv
total_rec = 0

#this is setting up a dfferent emepty lists

fNames = []
lNames = []
fnum = []
fbeast = []


with open("SE126/Week2/demo/w2d2_demoTextFile.txt") as textFile:
    #must have an indentaton for the file

    file = csv.reader(textFile)

    for rec in file:

        print(rec)

        #append field data to the right list
        fNames.append(rec[0])
        lNames.append(rec[1])
        fnum.append(int(rec[2]))
        
        #len() -- buit in function for the length of a struture(list)
        #the maximum length of rec is: 4 

        if len(rec) == 4:
            fbeast.append(rec[3])
        else: #rec does not exest and was never real
            fbeast.append("-NA-")


#process fnames + fbeast list to display
for index in range(0, len(fNames)):
    print(f"{fNames[index]}'s fav anial is: {fbeast[index]}")

