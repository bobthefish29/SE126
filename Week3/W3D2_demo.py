#most of this is juat a review but im board so im going to copy
#this will also have 2 d lists but thats later

import csv 

#making lists
#This is a group of 1D parallel lists
comp_type_list = []
manu_list = []
processor_list =[]
ram_list =[]
size_list = []
drive_list = []
hd2_list =[]
os_list = []
year_list = []

#making empty 2D lists
#combining all the parallel 1D lists
text_file_List = []





with open("SE126/Week3/filesWithText/lab2b.csv") as csvFile:

    file = csv.reader(csvFile)

    for rec in file:

        #2d lists
        text_file_List.append(rec)
        #text_file_List.append('D','DL','i5','08','001TB','1','W07','15')







        #this is what 1d lists look like
        comp_type_list.append(rec[0])
        manu_list.append(rec[1])
        processor_list.append(rec[2])
        ram_list.append(rec[3])
        size_list.append(rec[4])

        if rec[5] == "2":
            drive_list.append(rec[5])
            hd2_list.append(rec[6])
            os_list.append(rec[7])
            year_list.append(rec[8])
        elif rec[5] == "1":
            drive_list.append(rec[5])
            hd2_list.append("---")
            os_list.append(rec[6])
            year_list.append(rec[7])
        else:
            drive = "Error" + str(rec[5])
            hd2 = "---"
            os = "Error"
            year = "error"

#-----------------------------------

for i in range(0, len(comp_type_list)):
    print(f"{comp_type_list[i]} {drive_list[i]} {year_list[i]}")

#this is 2d list processing
print("\n------------2D list------------\n")
for i in range (0, len(text_file_List)):

    print(f"Line {i+1}:  {text_file_List[i]}")

    #have to used different index value or you in loop
    for x in range(0, len(text_file_List[i])):

        #the first i is for what recored, x is for what location in that recored
        print(f"{text_file_List[i][x]}", end=" - ")

    #give space for the next data
    print()