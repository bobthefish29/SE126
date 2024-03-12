#Binary Search Algorithm:
#This is the code for the binary search,  need to

#this is what we are looking for
search = input("Get search from user!")

#the lowest index in that list and the lowest point
min = 0
#the max number of 
max = len(records - 1)       #can also use len(listName) for 'records' value

#this is the midpoint to see if its on one half or the other
mid = int((min + max) / 2)

#this is for INCREASING order
#this is for whne the min number is less than the max number and "search" does not equal the value at mid ----look again----
while (min < max and search != listName[mid]):
    #This is for if the search is the 
    if search < listName[mid]:

        max = mid - 1

    else:

        min = mid + 1

    mid = int((min + max) / 2)

if search == listName[mid]:
    print()
    #found them! use 'mid' for index of found search item

else:

    #boooo not found
    print()