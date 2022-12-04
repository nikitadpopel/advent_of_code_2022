import sys
sys.path.append('../')
from helper_functions import *

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
    lineList = readInput('../inputs/day1.txt')
    print(part1(lineList))
    print(part2(lineList))