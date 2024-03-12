#this is the week 7 demo 

#Using the different search methodes to be able to find the information

#------------------Imports
import csv


#--------------------Functions----------------


#------------Main-code------------------
id_stud = []
fname = []
lname = []
class1 = []
class2 = []
class3 = []

with open("Week7/Textfile/w7_demoFile.txt") as csvFile:

    file = csv.reader(csvFile)

    for rec in file:
        id_stud.append(rec[0])
        fname.append(rec[2])
        lname.append(rec[1])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

#checking if its working

for i in range(0, len(id_stud)):
    print(f"{fname[i]} {lname[i]}")

#looking through the search to find the product


searchName = input("\n\nseqSearch-What whould you class to search for: ")
#found = -1
found = [] #having the list
seq_search = 0
#Search
for i in range(0, len(lname)):
    seq_search += 1
    #Asking if the search name at that index to be the same thing
    if searchName.lower() == lname[i].lower():
        #storing the data to a location (index)
        #if it finds it than there
        found.append(i)
#outPut
print (f"The projram went through {seq_search} times ")
#if found[0] != "":
    #print(f"The person {searchName} was at index {found}")
    #for i in range(0, len(found)):
        
        #print(f"There name is {fname[found[i]]} {lname[found[i]]} \n{class1[found[i]]} \n{class2[found[i]]} \n{class3[found[i]]}")
#else:
    #print(f"There is no person with the name {searchName}")
    #print("Enter the ---name--- you want to use.")



#binary search -----deviding the order into 2 sections based on the search pool, higher, lower
searchName = input("\n\nBinary-What whould you Last Name to search for: ")
min = 0 #the first spot for the search
max = len(lname) - 1#taking away 1 because the lis does not go up to 26 only 25 in this case
#mid = int((0 + (len(lname) - 1)) / 2 )
mid = int((min + max) / 2)
binCount = 0#just a count for the total times it then through
#THis is the search idea
while(min < max and searchName.upper() != lname[mid].upper()):
    binCount += 1
    if searchName.upper() < lname[mid].upper():
        max = mid - 1
    else: 
        min = mid +1
    mid = int((min + max) / 2)
if searchName.upper()== lname[mid].upper():
    #Found them
    print(f"There name is {fname[mid]} {lname[mid]} \n{class1[mid]} \n{class2[mid]} \n{class3[mid]}")
else:
    #not foundsorry
    print(f"There is no person with the name {searchName}")
    print("Enter the ---name--- you want to use.")




input("\n\n\tl------------About to bubble sort------------")
#BUBBLE SORT----------------------------------------

nums = [100, 75, 32, 250, 47, 9, 2, 3, 99, 200]

print(F"CurrentList: {nums}")



#bubble sort algorithm 
for i in range(0, len(nums) - 1):#outter loop
    print("OUTER LOOP! i = ", i)

    for index in range(0, len(nums) - 1):#inner loop

        print("\t INNER LOOP! k = ", index)
        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing
        if(nums[index] > nums[index + 1]):

            print(f"\t\t SWAP! {nums[index]} <--> {nums[index + 1]}")

            #if above is true, swap places!

            temp = nums[index]
            nums[index] = nums[index + 1]
            nums[index + 1] = temp

            #swap all other values

            #temp = age[index]

            #age[index] = age[index + 1]

            #age[index + 1] = temp

print(f"Sorted List; {nums}")