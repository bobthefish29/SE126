#Week 3 Day one demo - handling a test file
import csv

#need a total counter
total_count = 0

#this is the list for every entrey in the list that is there
comp_type_list = []
manu_list = []
processor_list =[]
ram_list =[]
size_list = []
drive_list = []
hd2_list =[]
os_list = []
year_list = []



print("Type\t Brand\t\tCPU\tRam\t1 Disk\tHHD?\t2 Disk\t Os\tYear")
print("-----------------------------------------------------------------------")
with open("SE126/Week3/filesWithText/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #print(rec) #this will show as a list[]

        #keeping track of the rec in the file
        total_count += 1

        if rec[0] == "D":
            comp_type = "DeskTop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "-Error-" + str(rec[0])

        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "GateWay"
        elif rec[1] == "HP":
            manu = "Hp"
        else:
            manu = "-error-" + str(rec[0])



        pross = rec[2]
        ram = rec[3]
        size = rec[4]


        #drive = rec[5]




        if rec[5] == "2":
            drive = rec[5]
            hd2 = rec[6]
            os = rec[7]
            year = rec[8]


        elif rec[5] == "1":
            drive = rec[5]
            hd2 = "---"
            os = rec[6]
            year = rec[7]

        
        else:
            drive = "Error" + str(rec[5])
            hd2 = "---"
            os = "Error"
            year = "error"

        #append all the recoreds in the list, adding the value of the name Ex. comp_type will be in the list comp_type_list
        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processor_list.append(pross)
        ram_list.append(ram)
        size_list.append(size)
        drive_list.append(drive)
        hd2_list.append(hd2)
        os_list.append(os)
        year_list.append(year)


        print(f"{comp_type:8}\t {manu:10}\t {pross:5}\t {ram:5}\t {size:5}\t {drive:5}\t {hd2:5}\t {os:5}\t {year:5}")
#Out of file-----------------------------------------------------------------
print("-----------------------------------------------------------------")
print(f"Total Records: {total_count}")


#appending the lists to print the data

for index in range(0, total_count):
    #this could also be in range(0, len(comp_type_list)): This would also run for the total recoreds in the file.
    print(f"E{comp_type_list[index]:4}\t {manu_list[index]:7}\t {processor_list[index]:2}\t {ram_list[index]:2}\t {size_list[index]:5}\t {drive_list[index]:5}\t {hd2_list[index]:5}\t {os_list[index]:5}\t {year_list[index]:5}")


#this is help for the lab that we are going to be duing due friday

#precess the list to cound the num of desktops
desktop_count = 0
value = 0

for index in range(0, len(comp_type_list)):

    if comp_type_list[index] == "DeskTop" and int(year_list[index]) <= 16:
        desktop_count += 1

value = desktop_count * 2000


print(desktop_count , value)


#precss  the list to find avarage size

total_size = 0
count_size = 0

for index in range(0, len(size_list)):

    if size_list[index] == '001TB':
        total_size += 1
    else:
        total_size += 0.5

    count_size += 1

average = total_size / count_size #could also use 'len(size_list) or total_recoreds in place of count_size

print(f"avarage {average:0.2f}Tb or {average*1000:02.2f}GB")