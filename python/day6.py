import sys
sys.path.append('../')
from helper_functions import *

def unique(mystr):
    characterset = set()
    for charac in mystr:
        if charac in characterset:
            return False
        characterset.add(charac)
    return True

def part1(lineList):
    for i in range(len(lineList[0])-3):
        if unique(lineList[0][i:i+4]):
            return i + 4


def part2(lineList):
    for i in range(len(lineList[0])-13):
        if unique(lineList[0][i:i+14]):
            return i + 14

if __name__ == '__main__':
    lineList = readInput('../inputs/day6.txt')
    print(part1(lineList))
    print(part2(lineList))