# Day 2
# Part One

read_file = open('input.txt', 'r', encoding='utf-8')
data = list(map(str,read_file.read().split('\n')))

fwd = 0
depth = 0

for item in data:
    direction, num = item.split()
    match direction:
        case "forward":
            fwd += int(num)
        case "down":
            depth += int(num)
        case "up":
            depth -= int(num)
        case _:
            print("Error")
print("Part One: ", fwd * depth)

# Part Two

read_file = open('input.txt', 'r', encoding='utf-8')
data = list(map(str,read_file.read().split('\n')))

fwd = 0
aim = 0
depth = 0

for item in data:
    direction, num = item.split()
    match direction:
        case "forward":
            fwd += int(num)
            depth += (aim * int(num))
        case "down":
            aim += int(num)
        case "up":
            aim -= int(num)
        case _:
            print("Error")
print("Part Two: ", fwd * depth)
