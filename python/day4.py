import sys
sys.path.append('../')
from helper_functions import *

def getRange(line):
    mylist = []
    nums = line.split('-')
    for i in range(int(nums[0]), int(nums[1]) + 1):
        mylist.append(i)
    return mylist

def part1(lineList):
    count = 0
    for i in lineList:
        line = i.split(',')
        line1 = getRange(line[0])
        line2 = getRange(line[1])
        if all(item in line1 for item in line2) or all(item in line2 for item in line1):
            count += 1
    return count

def part2(lineList):
    count = 0
    for i in lineList:
        line = i.split(',')
        line1 = getRange(line[0])
        line2 = getRange(line[1])
        if any(item in line1 for item in line2) or any(item in line2 for item in line1):
            count += 1
    return count

if __name__ == '__main__':
    lineList = readInput('../inputs/day4.txt')
    print(part1(lineList))
    print(part2(lineList))