lines = []

with open("input.txt", "r") as file:
    lines = [line.split() for line in file]

lines = [list(map(int, i)) for i in lines]

def check_safe(reports):

    safe = True
    inc = None

    if len(reports) < 2:
        return False

    for i in range(len(reports)-1):
        if not safe:
            break
        inc_logic = reports[i] < reports[i+1]
        dec_logic = reports[i] > reports[i+1]
        stag_logic = reports[i] == reports[i+1]   

        if (i == 0):
            if inc_logic:
                inc = True
            elif dec_logic:
                inc = False
            elif stag_logic:
                inc = None


        # main logic
        if ((inc) and ((dec_logic) or (stag_logic))) or ((not inc) and ((inc_logic) or (stag_logic))):
            #unsafe due to increase decrease logic
            safe = False
        else:
            # safe from increase decrease logic
            # check if safe from increment amount logic
            offset = abs(reports[i] - reports[i+1])
            if offset > 3 or offset == 0:
                safe = False
    #if (safe):
        #print(f"DEBUG: We have a safe report: {reports}")

    
    return safe

# bool
def dampened_report(reports):
    if check_safe(reports):
        return True

    safe = False

    # main logic
    for i in range(len(reports)):
        #remove a level and check if safe
        mod_report = reports[:i] + reports[i+1:] 
        # ^nice little trick to slice the array and run through removing one element at a time and checking if its safe without the element
        # ex arr [1,2,3,4,5], -> [1,2,4,5] and now check if it works
        if check_safe(mod_report):
            safe = True
        
    return safe





def part1():
    safe_count = 0
    for i in range(len(lines)):
        safe_count += 1 if check_safe(lines[i]) else 0
    print(f"Safe report count: {safe_count}")


def part2():
    safe_count = 0
    for i in range(len(lines)):
        safe_count += 1 if dampened_report(lines[i]) else 0
    print(f"Safe report count: {safe_count}")



part1()
part2()