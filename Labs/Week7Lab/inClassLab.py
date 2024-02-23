#David punchak
#SE126
#2/23/2024
#Lab 5 [solo lab]


#---------------Notes-----------
#i added every search to a function
#in the 4 option it does not return to the menu, it just asks the user there if they want to look again.
#Adding the binary function was not as hard as i thought it would be
#i also have the clear to make things look nice


###############---Project discription---############

##This is a menu driven program it
#it will have 5 options based on the users input
#1 all records(Normal output) #Done
#2 Look for a student by id(Ask for student id return the rec location)  #done
#3 look for student by last name(ask for last name return rec location)  #done
#4 Veaw a class roster(ask for class number return every kid in that class) #done
#5 quit the project #done

#Bonus if you make a binary search #done

########--Importing---#####
import csv
from os import system, name 
#######-------#########

###############----Setting the varablues and lists----##############
userInput = 0
studentId = []
lName = []
fName = []
class1= []
class2 = []
class3 = []
#######################opening the csvFiles and appending them to the list##################################
with open("Labs/TextFiles/w7_demoFile.txt") as csvFile:


    file = csv.reader(csvFile)

    for rec in file:
        studentId.append(rec[0])
        lName.append(rec[1])
        fName.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

############################### Def the functions ######################
#just a clear function
def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#This is the menu 
def menu():

    print("--------------------------------------------------------------")
    print("\t1. See all student data")
    print("\t2. Search for Student [Id]")
    print("\t3. Search for Student [by Last name]")
    print("\t4. View Class Roster [Class ID]")
    print("\t5. Quit my project")
    print("--------------------------------------------------------------")
    pick = input("\n\nWhat would you like to do user: ")

    while pick != "1" and pick != "2" and pick != "3" and pick != "4" and pick != "5":
        print("\n----------Wrong Input----------")
        pick = input("\nWhat would you like to do user(1-5)")
    
    pick = int(pick)
    clear()
    return pick

#just a function to print the first output
def firstPick():
    #this is just to print every person 
    print("You have chosen to look at all the data\n")
    print(f"{'StudentId':8} | {'First Name':10} {'last Name':10} | {'Class1':6} {'Class2':6} {'Class3'}")
    print("-----------------------------------------------------------")
    for i in range(0, len(studentId)):
        print(f"{studentId[i]:9} | {fName[i]:10} {lName[i]:10} | {class1[i]:6} {class2[i]:6} {class3[i]}")
    #just to keep it neet and clean stoping the console than clearing it 
    input("\n-----------------Press Enter----------------------------")
    clear()

#this is the function for the binary search
def binarySearch(userPick):
    #setting the user pick to the value that would be used in the if else
    pick = userPick
    #this is just to see if they want to do it again with out going to the menu
    search = "y"
    while search.lower() == "y":
        #this is the type of search the user is doing
        if pick == 3:#this is for the last name search
            searchName = input("\n\nWhat -Last- name would you like to look for?: ")
            min = 0 #the first spot for the search
            max = len(lName) - 1 #taking away 1 because the lis does not go up to 26 only 25 in this case
            mid = int((min + max) / 2)
            while(min < max and searchName.lower() != lName[mid].lower()):
                if searchName.lower() < lName[mid].lower():
                    max = mid - 1
                else: 
                    min = mid +1
                mid = int((min + max) / 2)
            if searchName.lower() == lName[mid].lower():
                #Found them
                
                print(f"\nThere name is {fName[mid]} '{lName[mid]}'\nStudentId = {studentId[mid]} \n--Class's--\nclass1: {class1[mid]} \nClass2: {class2[mid]} \nClass3: {class3[mid]}")
            else:
                #not foundsorry
                print(f"\nThere is no person with the -last- name '{searchName}'")
                print("You might have typed it wrong?")
        


        else:#this is for the student id search
            searchName = input("\n\nWhat studentId are you looking for?: ")
            min = 0 #the first spot for the search
            max = len(studentId) - 1 #taking away 1 because the lis does not go up to 26 only 25 in this case
            mid = int((min + max) / 2)
            while(min < max and searchName != studentId[mid]):
                if searchName < studentId[mid]:
                    max = mid - 1
                else: 
                    min = mid +1
                mid = int((min + max) / 2)
            if searchName == studentId[mid]:
                #Found them
                print(f"\nThere name is {fName[mid]} {lName[mid]} \nStudentId = '{studentId[mid]}' \n--Class's--\nclass1: {class1[mid]} \nClass2: {class2[mid]} \nClass3: {class3[mid]}")
            else:
                #not foundsorry
                print(f"\nThere is no person with the -StudentId- '{searchName}'")
                print("StudentId Ex: '1234' ")
                

        search = input("\nwish to look again?: ")
        while search.lower() != "n" and search.lower() != "y":
            print("\n\t---------Enter(Y \ N) user------")
            search = input("\nwish to look again?: ")
    clear()

#this is the class search function
def clasSearch(): #it does not return the user to the menu after but ask them here if they want another
    #has the user pesponce
    answer = "y"
    while answer.lower() == "y":
        #This is the search than adding it to a list
        search = input("What class would you like to look for?: ")
        found = []
        for i in range(0, len(class1)):
            #adding to the list at that index
            if search.lower() == class1[i].lower() or search.lower() == class2[i].lower() or search.lower() == class3[i].lower():
                found.append([studentId[i], fName[i], lName[i]])
        #if the len of found is 0 than there was no class or person in that class. 
        if len(found) >= 1:
            print(f"\n{'StudentID':10} | {'First Name':13} | {'Last Name'}")
            print("--------------------------------------------------------")
            for i in range(0, len(found)):
                print(f"{found[i][0]:10} | {found[i][1]:13}   {found[i][2]}")
                
        else:
            print(f"\nThere is o class named / No one in: {search}")

        #Getting the user reply to see if they want to do it again
        answer = input("\nWish to look up a different class: ")
        while answer.lower() != "n" and answer.lower() != "y":
            print("\n\t---------Enter(Y \ N) user------")
            answer = input("\nWish to look up a different class?: ")

        clear()

####################---Main Code---#####################
print("\t\tWelcome user to my project")

#main while loop for the user
while userInput != 5:

    #the menu and getting the input and casting as a number
    userInput = int(menu())

    if userInput == 1:
        #pick one
        firstPick()
    elif userInput == 2:
        #pick 2
        binarySearch(userInput)
    elif userInput == 3:
        #pick 3
        binarySearch(userInput)
    elif userInput == 4:
        #pick 5
        clasSearch()
    else:
        #this is for any other pick but it can only be 5
        print("\n\n\t---Thank you for using my program :}---")

#Out of main code end of project.
input("\n\t--------------------Please press 'Enter' to quit---------------------------")
clear()