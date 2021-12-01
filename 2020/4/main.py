file1 = open('/2020/4/input.txt', 'r')

# count = 0
# ar=[]
# x=""
# dict={}
# con="byr,iyr,eyr,hgt,hcl,ecl,pid"
# count=0
# x=file1.read()
# for spl in x.split("\n\n"):
#     score=0
#     for y in con.split(","):
#         if y in spl:
#             score+=1
#     if score>=7:
#         count+=1
# print(count)

def check(x):
    if(x.split(":")[0]=="ecl"):
        if(x.split(":")[1]==""):
            return 1
    if(x.split(":")[0]=="byr"):
        if(1920<=x.split(":")[1]<=2020):
            return 1

    if(x.split(":")[0]=="eyr"):
        if (x.split(":")[1] == ""):
            return 1
    if(x.split(":")[0]=="pid"):
        pass
    if(2010<=x.split(":")[0]=="iyr"<=2020):
        pass
    if(x.split(":")[0]=="hgt"):
        if ("cm" in x.split(":")[1]):
            if(150<=x.split(":")[1][0:3]<=193):
                return 1
        elif("in" in x.split(":")[1]):
            if(59<=x.split(":")[1][0:3]<=76):
                return 1
    if(x.split(":")[0]=="ecl"):
        pass

count = 0
ar=[]
x=""
dict={}
con="byr,iyr,eyr,hgt,hcl,ecl,pid"
count=0
total=0
i=0
x=file1.read()
for spl in x.split("\n\n"):
    score=0
    for y in con.split(","):
        if y in spl:
            score+=1
    if score>=7:
        for s in spl.split(" "):
            count+=check(s)
            #print(s)
        if count>=7:
            count=0
            total+=1

       # print("---------------")
print(total)
