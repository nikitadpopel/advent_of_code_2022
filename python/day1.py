def readInput(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def part1(lineList):
    elves = []
    elf = 0
    for i in lineList:
        if i != '':
            elf += int(i)
        else:
            elves.append(elf)
            elf = 0
    elves.sort()
    return elves[-1]


def part2(lineList):
    elves = []
    elf = 0
    for i in lineList:
        if i != '':
            elf += int(i)
        else:
            elves.append(elf)
            elf = 0
    elves.sort()
    return elves[-1] + elves[-2] + elves[-3]

if __name__ == '__main__':
    lineList = readInput('day1.txt')
    print(part1(lineList))
    print(part2(lineList))