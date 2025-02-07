import re

data = ''
with open('input.txt', 'r') as file:
    data = file.read()

def part1():
    pattern = r"mul\([0-9]+,[0-9]+\)"
    matches = re.findall(pattern, data)
    sum = 0
    for match in matches:
        # match the integers inside individual mul() now
        num_arr = re.findall(r'\d+' , match)
        sum += int(num_arr[0]) * int(num_arr[1])
    
    print(sum)
        

def part2():
    allow = True
    sum = 0

    exp = re.finditer(r"(do\(\))|(don't\(\))|(mul\([0-9]+,[0-9]+\))", data)

    for i in exp:
        if i.group(1):
            allow = True
        elif i.group(2):
            allow = False
        elif i.group(3):
            if allow:
                num_arr = re.findall(r'\d+', i.group(3)) 
                sum += int(num_arr[0]) * int(num_arr[1]) 

    print(sum)


part1()
part2()