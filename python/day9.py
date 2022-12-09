import sys
sys.path.append('../')
from helper_functions import *
import time

class Bridge:
    def __init__(self):
        self.xwidth = 1
        self.ywidth = 1
        self.head = {'x':0,'y':0}
        self.tail = {'x':0,'y':0}
        self.spaces = {0:{0:'hello', 1:'bye'}}
    def printSpaces(self):
        for i in self.spaces:
            for j in self.spaces[i]:
                print(self.spaces[i][j])
                

def part1(lineList):
    bridge = Bridge()
    bridge.printSpaces()
    for i in lineList:
        print(i)

def part2(lineList):
    pass

if __name__ == '__main__':
    lineList = readInput('../inputs/day9.txt')
    print(part1(lineList))
    print(part2(lineList))