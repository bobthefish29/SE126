#w5D1 -1d list revie and some new search things


import csv

#making new lists
#from file

fname = []
lname = []
test1 = []
test2 = []
test3 = []

numAvg=[]
letAvg=[]


#------functions-----------

def menu():
    
    print("~User menu~")
    print("1. SHOW All Students")
    print("2. SHOW Just name")
    print("3. Looking for Student")
    print("4. EXIT")

    choice = int(input("Please enter your selecton [1 - 4]: "))

    while choice < 0 or choice > 4:
        print("----------Error----------")
        choice = int(input("Please enter your selecton [1 - 4]: "))


    return choice
    
def seqSearch(search_term):
    #the search term is what we are lookng for

    
    #initialize found index variable found_index as a local value

    found_index = ""


    #sequence search - Start at beginning (0) go to the end (len(listname))
    for i in range(0,len(lname)):
        #look a each value in the fname list
        if lname[i] == search_term:
            found_index = i #storing the value at index to the list if it is the name

    return found_index






#---------connecting to other files
with open("SE126/Week5/week5_listReview/week5_listReview/listPractice1.txt") as csvFile:

    file = csv.reader(csvFile)

    for rec in file:

        #adding the rec to the file, 
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#out of the loop
print("{'fname':12}{'lname':12}\t{'test1':4}\t{'test2':4}\t{'test3':4}\t {'numAvg':5.1f} \t {'letAvg':3}")
print("---------------------------------------------------------------------------------------------------")

#making another list for num and let avg

for i in range(0,len(fname)):
    grade_sum = test1[i] + test2[i] + test3[i]

    grade_avg = grade_sum / 3 

    numAvg.append(grade_avg)

    if grade_sum >= 90:
        letter="A"
    elif grade_sum >= 80:
        letter = "B"
    elif grade_sum >= 70:
        letter = "C"
    elif grade_sum >= 60:
        letter = "D"
    elif grade_sum < 60:
        letter="F"
    else:
        letter = "ERROR @ i :" + str(i)

    letAvg.append(letter)


#testing 
for i in range(0,len(lname)):
    print(f"{fname[i]:12} {lname[i]:12} \t{test1[i]:6} \t{test2[i]:6} \t{test3[i]:6}\t {numAvg[i]:5.1f} \t {letAvg[i]:3}")
print("------------------------------------------------------------------------------------------")
#--------------main code-------------


#allowing user to si

menu_choice = menu()

while menu_choice != 4: #exit

    #determin what the user wants to do
    if menu_choice == 1:
        print("\n\t--Show all file data--")
    elif menu_choice == 2:
        print("\n\t--Showing class roster (Names)--")
    else: #menu_choice == 3:
        print("\n\t--Search for student--")
        search = input("Enter the last name you are looking for: ")
        #this is going to be the index number
        found = seqSearch(search)

        
        if found != "":
            print(f"{fname[found]:12} {lname[found]:12} \t{test1[found]:6} \t{test2[found]:6} \t{test3[found]:6}\t {numAvg[found]:5.1f} \t {letAvg[found]:3}")

        else:
            print(f"You silly the student {search} was not found, are they even real?? ")


    #let user do newthing
    menu_choice = menu()
    
print("\n\n\tThank you for using my project")

input("-------------------------Press Enter to quit----------------------------")


