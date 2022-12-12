import sys
sys.path.append('../')
from helper_functions import *
import math
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
        if direction == 'L':
            self.head['x'] += -1
        if direction == 'U':
            self.head['y'] += 1
        if direction == 'R':
            self.head['x'] += 1
        if direction == 'D':
            self.head['y'] += -1
        pass

    def moveTail(self):
        if (abs(self.head['x'] - self.tail['x']) == 2 and abs(self.head['y'] - self.tail['y']) == 1) or (abs(self.head['x'] - self.tail['x']) ==1  and abs(self.head['y'] - self.tail['y']) == 2):
            temp1 = self.head['x'] - self.tail['x']
            temp2 = self.head['y'] - self.tail['y']
            if temp1 < 0:
                self.tail['x'] += int(temp1 * (-1 / temp1))
            else:
                self.tail['x'] += int(temp1 * (1 / temp1))
            if temp2 < 0:
                self.tail['y'] += int(temp2 * (-1 / temp2))
            else:
                self.tail['y'] += int(temp2 * (1 / temp2))


        elif abs(self.head['x'] - self.tail['x']) > 1:
            self.tail['x'] += int(self.head['x'] - self.tail['x'])/2
        elif abs(self.head['y'] - self.tail['y']) > 1:
            self.tail['y'] += int(self.head['y'] - self.tail['y'])/2
        
        self.tail['x'] = int(self.tail['x'])
        self.tail['y'] = int(self.tail['y'])
        spacestr = str(self.tail['x']) + ' ' + str(self.tail['y'])
        self.spaces[spacestr] = 1
        pass

    def move(self, line):
        splitline = line.split(' ')
        for i in range(int(splitline[1])):
            self.moveHead(splitline[0])
            self.moveTail()
        

                

def part1(lineList):
    bridge = Bridge()
    for i in lineList:
        bridge.move(i)
    return len(bridge.spaces)

def part2(lineList):
    pass

if __name__ == '__main__':
    lineList = readInput('../inputs/day9.txt')
    print(part1(lineList))
    print(part2(lineList))