#David punchak
#SE116 int-mid python
#1/30/24



#This is like the demo we did in class but we need to have a few different changes

#The final outputs need to be a basic list, a list with the average number of scores and the letter grade that goes with it

#the last part we need to have a 2D list that is holding all the data that we found 


#####################################################

#so um a lot of this is just copy from the week 4 day 1 demo but i has parts that are different, ill add a comment when i go in a change it from the demo 

###############################################################





import csv

#making lists here
#This is a 1 d list that just have []

fName = []
lName = []
test1 = []
test2 = []
test3 = []

#opping the file

with open("SE126/Week4/TextFile\listPractice1-1.txt") as csvFile:

    file = csv.reader(csvFile)

    for rec in file:
        #print(rec)--->this is how to find a error if the index is out of sync/List out of index
        #storing the data to the list that the field is about
        #this is an example of an parallel list because we are storing the data to the index and its just having the data that belongs together
        #this is adding the rec value to the list that is there
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))#the 'int' is setting the numbers to be numbers and not string values.
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#this is just some print for the user to see in a nice look
print("First name \t Last Name \t 1st Test \t 2nt test\t 3rd test\t")
print("-----------------------------------------------------------------------------")
#this is a loop for display
for i in range(0, len(fName)):
    print(f"{lName[i]:12} \t {fName[i]:12}  \t {test1[i]} \t\t {test2[i]} \t\t {test3[i]}")
print("----------------------------------------------------------------------------")

#this is some of the new vars and lists for the averages
avg = 0
total_count = 0
class_avg = 0

#new lists
average = []
letter_avg = []

#this is the main for loop that does the math and getting the letter value
for i in range(0, len(test1)):

    #doing the math for the avarage and adding the avg to the total class avg
    avg = (test1[i] + test2[i] + test3[i]) / 3 
    class_avg = class_avg + avg

    #adding the average to the list
    average.append(avg)

    #this is me, this was not in the demo that you had us do
    if avg >= 90 and avg <= 100:#if it is 90 - 100 it is an A and so on
        letter_avg.append("A")
    elif avg >= 80 and avg <= 89:
        letter_avg.append("B")
    elif avg >= 70 and avg <= 79:
        letter_avg.append("C")
    elif avg >= 60 and avg <= 69:
        letter_avg.append("D")
    else:
        letter_avg.append("F")


    #just printing random things that might be trashed
    print(f"{fName[i]} has a {average[i]:.1f} that is a {letter_avg[i]}")
    total_count += 1

#doing the math for the class total average
class_avg = class_avg / total_count

print(class_avg)

#this is going to the place were i have the displayes for the 2D list

