import csv

total = 0




with open() as he:

    file = csv.reader(he)

    for rec in file:


        if rec[0] == "D":
            comp_type = "DeskTop"
        elif rec[0] == "L":
            comp_type = "LapTop"
        else:
            comp_type = "-Error-"


        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:



        pross = rec[2]
        ram = rec[3]
        size = rec[4]
        drive = rec[5]

#f rec[5] == 2 than we make rec6 to the one down the line rec[8] would be year, else rec5 would be blank is os and rec [7] is year



        print(rec)
        print(f"{comp_type} {manu} {pross} {ram} {size} {drive} {hd2} {os} {year}")

        