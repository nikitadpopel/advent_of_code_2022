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
        self.spaces = {}
    def printStuff(self):
        print(self.head)
        print(self.tail)
        print(self.spaces)


    def moveHead(self, direction):
        print('moving head in ' + direction)
        pass

    def moveTail(self):
        print('moving tail')
        pass

    def move(self, line):
        splitline = line.split(' ')
        for i in range(int(splitline[1])):
            self.moveHead(splitline[0])
            self.moveTail()
        

                

def part1(lineList):
    bridge = Bridge()
    bridge.printStuff()
    for i in lineList:
        bridge.move(i)
        bridge.printStuff()

def part2(lineList):
    pass

if __name__ == '__main__':
    lineList = readInput('../inputs/day9.txt')
    print(part1(lineList))
    print(part2(lineList))