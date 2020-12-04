file1 = open('C:\\Users\\adminpk\\PycharmProjects\\advent_of_code\\1\\input.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
# Part1
for line1 in Lines:
    for line2 in Lines:
        #for line3 in Lines: #Part 2
            #if int(line1)+int(line2)+int(line3)== 2020: #Part 2
            if int(line1)+int(line2)== 2020:
                print(line1,line2)
                #print(line1,line2,line3) #Part 2
                print(int(line1)*int(line2))
                #print(int(line1)*int(line2)*int(line3)) #Part 2