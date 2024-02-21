#This is the demo for class week 7 day 2

import csv


#the lists for the list
type = []
name = []
mean = []
org = []



with open("SE126/Week7/Textfile/party.csv", encoding = "utf-8") as csvFile:
    file = csv.reader(csvFile)

    for rec in file:
        type.append(rec[0])
        name.append(rec[1])#best thing to sory and search by because in this list there is no different values.
        mean.append(rec[2])
        org.append(rec[3])


##sort the file data by first name , asending (increasing in order)
print(f"{'type':10} {'name':12} {'mean':30} {'org'}")
print("--------------------------------------------------------------------------------------")
#og file print
for i in range(0, len(type)):
    print(f"{type[i]:10} {name[i]:12} {mean[i]:30} {org[i]}")
print("--------------------------------------------------------------------------------------")


#need to sort the values throught bubble sort-------------------------------
for i in range(0, len(name) - 1):#outter loop
    for index in range(0, len(name) - 1):#inner loop

        if(name[index] > name[index + 1]):
            #if above is true, swap places! this is what we want to search by
            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp

            #swaping other data
            #Type swap
            temp = type[index]
            type[index] = type[index + 1]
            type[index + 1] = temp

            #meaning swap
            temp = mean[index]
            mean[index] = mean[index + 1]
            mean[index + 1] = temp

            #origin swap
            temp = org[index]
            org[index] = org[index + 1]
            org[index + 1] = temp


print("\t\t----------After sort-------------")
#testing data to see the order
print(f"{'type':10} {'name':12} {'mean':30} {'org'}")
print("--------------------------------------------------------------------------------------")
#og file print
for i in range(0, len(type)):
    print(f"{type[i]:10} {name[i]:12} {mean[i]:30} {org[i]}")
print("--------------------------------------------------------------------------------------")


#this is going to be binary search-------------------------------

answer = "y"

while answer.lower() == "y":
    search = input("Get search from user!")
    min = 0
    max = len(name) - 1   #can also use len(listName) for 'records' value
    mid = int((min + max) / 2)

    while (min < max and search.lower() != name[mid].lower()):
        
        if search < name[mid]:
            max = mid - 1

        else:

            min = mid + 1

        mid = int((min + max) / 2)
    #lower here for the values to have 
    if search.lower() == name[mid].lower():
        print(f"\n\tWE found {search}! The info is")
        print(f"{'type':10} {'name':12} {'mean':30} {'org'}")
        print(f"{type[mid]:10} {name[mid]:12} {mean[mid]:30} {org[mid]}")

    else:
        print(f"\n\tWE did not find {search}! The info is")


    answer = input("Would you like to look again(Y/N): ")