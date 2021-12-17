
def first():
    f = open("9.input", "r", encoding="UTF-8")
    array=[]
    for line in f.readlines():
        array.append(list(line.replace("\n","")))
    print(array)


first()