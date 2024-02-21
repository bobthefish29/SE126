#BUBBLE SORT----------------------------------------


#This is for running the sort for each number in the value
for i in range(0, number_of_elements - 1):#outter loop

    #print("OUTER LOOP! i = ", i)

    #this is the loop for moving the number to the right place, 
    for index in range(0, number_of_elements - 1):#inner loop

        #print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        #this is if the number or value is less than it would move down but if its more than it would move to start
        #the <> here is to have the list higher to lower or lower to higher
        if(name[index] > name[index + 1]):

            #print("\t\t SWAP! ", name[index], "<-->", name[index + 1])

            #if above is true, swap places!
            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp


            #swap all other values
            temp = age[index]
            age[index] = age[index + 1]
            age[index + 1] = temp
