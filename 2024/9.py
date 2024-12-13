import decimal
import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])

def get_id_result(disk,start_code):
    result=0
    for i,letter in enumerate(disk):
        if letter!=".":
            x=ord(letter)-start_code
            result=result+int(ord(letter)-start_code)*i
    return result
def pretty_print_disk(disk,start_code):
    result=""
    for letter in disk:
        if letter==".":
            result=result+"."
        else:
            result=result+str(ord(letter)-start_code)
    return result
def first(verbose=False):
    file = open("9.input", "r")
    disk = ""
    id=0
    free_space = False
    free_space_count=0
    start_code=58
    while True:
        number = file.read(1)
        if number!="":
            if free_space:
                if number!=str(0):
                    disk=disk+(int(number)*".")
                    free_space_count=free_space_count+int(number)
            else:
                disk=disk + ((int(number)*(chr(start_code+id))))
                id=id+1
            free_space = not free_space
        if not number:
            break
    reverse_disk=disk[::-1]
    if verbose: print("Original disk: {}".format(disk))
    for i,letter in enumerate(reverse_disk):
        if letter!=".":
            if verbose: print("Insert {}".format(letter))
            disk=disk.replace(".",letter,1)
        if i==free_space_count-1:
            disk=disk[:len(disk)-free_space_count]+"."*free_space_count
            break
    if verbose: print("Result disk: {}".format(disk))
    if verbose: print("Pretty printed disk: {}".format(pretty_print_disk(disk,start_code)))
    return get_id_result(disk,start_code)


def second(verbose=False):
    file = open("9.input", "r")
    disk = ""
    id=0
    free_space = False
    free_space_count=0
    start_code=58
    dic={}
    free_spaces={}
    while True:
        number = file.read(1)
        if number!="":
            if free_space:
                if number!=str(0):
                    free_spaces[len(disk)]=int(number)
                    disk=disk+(int(number)*".")
                    free_space_count=free_space_count+int(number)
            else:
                disk=disk + ((int(number)*(chr(start_code+id))))
                if verbose: print("{} is {}".format(id,chr(start_code+id)))
                dic[chr(start_code+id)]=int(number)
                id=id+1
            free_space = not free_space
        if not number:
            break
    dic=dict(reversed(dic.items()))
    if verbose: print("Original disk {}".format(disk))
    if verbose: print("Original pretty disk: {}".format(pretty_print_disk(disk,start_code)))
    if verbose: print("Dictionary: {}".format(dic))
    if verbose: print("Free spaces: {}".format(free_spaces))
    for i,element in enumerate(dic.items()):
        for space in free_spaces.items():
            if element[1]<=space[1]:
                if verbose:print("Should put {} on index {}".format(element[0],space[0]))
                disk=disk[:space[0]]+element[0]*element[1]+disk[space[0]+element[1]:].replace(element[0],".")
                if element[1]<space[1]:
                    free_spaces.pop(space[0])
                    free_spaces[space[0]+element[1]]=space[1]-element[1]
                else:
                    free_spaces.pop(space[0])
                free_spaces=dict(sorted(free_spaces.items()))
                break
    if verbose: print("Pretty print disk: {}".format(pretty_print_disk(disk,start_code)))
    return get_id_result(disk,start_code)


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=False)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
