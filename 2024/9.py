import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])

def get_nearest_free_space(disk):
    for i,element in enumerate(disk):
        if "." in element:
            return i

def first(verbose=False):
    file = open("9.input", "r")
    disk = []
    id=0
    free_space = False
    free_space_count=0
    while True:
        number = file.read(1)
        if number!="":
            if free_space:
                if number!=str(0):
                    disk.append(int(number)*".")
                    free_space_count=free_space_count+int(number)
            else:
                disk.append((int(number)*(str(id)+"-"))[:-1])
                id=id+1
            free_space = not free_space
        if not number:
            break
    print(disk)
    reverse_disk=disk.copy()
    reverse_disk.reverse()
    element_count=0
    for element in reverse_disk:
        if element_count==free_space_count:
            break
        if "." not in element:
            if element_count + len(element.split("-"))>free_space_count:
                print("Should move {} but only {}".format(element,free_space_count-element_count))

                element_count=element_count+free_space_count-element_count
            else:
                element_count = element_count + len(element.split("-"))
                original_length=len(disk[get_nearest_free_space(disk)])
                if original_length>=len(element.split("-")):
                    disk[get_nearest_free_space(disk)]=element.replace("-","") + (original_length-len(element.split("-")))*"."
                    disk[disk.index(element)]=len(element.split("-"))*"."
                else:
                    original_element=element
                    while element!="":
                        if get_nearest_free_space(disk)==disk.index(original_element):
                            break
                        dot_count = disk[get_nearest_free_space(disk)].count(".")
                        disk[get_nearest_free_space(disk)]=disk[get_nearest_free_space(disk)].replace(".",element.split("-")[0])
                        element=element[:-2*dot_count]
                        disk[disk.index(original_element)] = element+(dot_count+original_element.count("."))*"."
                        original_element=element+(dot_count+original_element.count("."))*"."
    st=""
    for element in disk:
        st=st+element.replace("-","")
    summary = 0
    for i,char in enumerate(st):
        if char==".":
            break
        summary=summary+(i*int(char))
    print(disk)
    return summary


def second(verbose=False):
    file = open("9.input", "r")
    matrix = []
    summary = 0
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
