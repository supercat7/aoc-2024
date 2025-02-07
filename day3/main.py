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
        

part1()