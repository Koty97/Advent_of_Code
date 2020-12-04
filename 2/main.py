file1 = open('C:\\Users\\adminpk\\PycharmProjects\\advent_of_code\\2\\input.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
# Part1
#for line in Lines:
#   min = int(line.split(' ')[0].split('-')[0])
#    max = int(line.split(' ')[0].split('-')[1])
#    letter = (line.split(' ')[1].split(':')[0])
#    word = (line.split(' ')[2])
#    wc =word.count(letter)
#    if(min<=wc and wc<=max):
#        count+=1
    #print (min,max,letter,word)
#print (count)
#Part2
pwd_sum2=0
for line in Lines:
    i = int(line.split(' ')[0].split('-')[0])
    j = int(line.split(' ')[0].split('-')[1])
    letter = (line.split(' ')[1].split(':')[0])
    word = (line.split(' ')[2])
    if (word[i - 1] == letter and word[j - 1] != letter) or (word[i - 1] != letter and word[j - 1] == letter):
        pwd_sum2 += 1
print (pwd_sum2)