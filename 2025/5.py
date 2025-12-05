import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    fresh_id_pairs = []
    for line in file:
        line = line.strip()
        if "-" in line:
            split_line=line.split("-")
            fresh_id_pairs.append((int(split_line[0]),int(split_line[1])))
        elif line != "":
            y = len(list(filter(lambda x: x[0]<=int(line) and x[1]>=int(line),fresh_id_pairs)))
            if verbose: print(f"For {line} found {y}s")
            if y >0:
                 summary=summary+1
    if verbose: print(fresh_id_pairs)
    
    return summary


def second(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    fresh_id_pairs = []
    for line in file:
        line = line.strip()
        if "-" in line:
            split_line=line.split("-")
            fresh_id_pairs.append((int(split_line[0]),int(split_line[1])))
        else:
            break
    rr=fresh_id_pairs.copy()
    removed={}
    for pair in fresh_id_pairs:
        print(f"Processing pair {pair}")
        #a= list(filter(lambda x: x!=pair and ((x[0]<=pair[0] and x[1]>=pair[1]) or (x[0]<=pair[1] and x[1]>=pair[1])),fresh_id_pairs))
        a= list(filter(lambda x: x!=pair and ((x[0]<=pair[0] and x[1]>=pair[1])),fresh_id_pairs))
        b= list(filter(lambda x: x!=pair and ((x[0]<=pair[1] and x[1]>=pair[1])),fresh_id_pairs))
        c= list(filter(lambda x: x!=pair and ((x[0]==pair[1] or x[1]==pair[0])),fresh_id_pairs))
        #print(a)
        #print(b)
        #print(c)
        
        print(a or b or c)
        pass
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f"Took {time_end - time_start} seconds")