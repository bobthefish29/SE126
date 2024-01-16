import csv

#setting up the starting vals
#total records
total_rec = 0
#total sallaries
total_sal = 0

#int empty list - 1 list per field
names = []
age = []
sal = []

#this is the information on the starting title
print(f"{'Name':8} \t{'Age':3} \t${' Salary':10}")
print("-------------------------------")

with open("Week2/demo/example.csv") as csvFile:  #the csvFile name is what the varable is named
    
    #reading the file
    #file is setting the csvfile to be file
    file = csv.reader(csvFile)

    #go in and read each reccored in the file

    for rec in file: #this "file" is where the csv is being changes
        #for every recored field that will be an entire data fields

        #displaying the values in neat columnes
        print(f"{rec[0]:10} {rec[1]:5} ${float(rec[2]):10.2f}")

        #store data from rec list (recored being read) to a list that is being read
        #adding data to a list we use the .append(); requires list names

        names.append(rec[0])
        age.append(int(rec[1]))
        sal.append(float(rec[2]))
        #keeping a cound of the recordes
        total_rec += 1

        #keeing a count of the sal
        total_sal += float(rec[2])

print("--------------------------------")
print(f"Total records {total_rec} |Total sal $ {total_sal:.2f}")

#process the list to display the correct information
#we are going to use a for loop-------------------

for index in range(0, total_rec):
    #for each value in the range for 0 to 3 times resporented by total recordes.
    print(f"INDEX: {index} \t {names[index]} is {age[index]} years old")

#process throught the list to creat total age value

total_age = 0
for index in range(0, total_rec):
    #add each age to a total age variable
    total_age += age[index]

#determin the avaerage age and display
avarage_age = total_age / total_rec
print(f"Average age: {avarage_age:.2f} ")

#this is just a different way to add the ages to the total age
#total_age = 0
#index = 0
#while index < total_rec:
    #index += 1
    #total_age += age[index]