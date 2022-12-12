import sys
sys.path.append('../')
from helper_functions import *
import time

class Monkey:
    def __init__(self, startingitems, operationsign, operationconst,testdivisor,truecondition,falsecondition):
        self.counttimes = 0
        self.items = []
        for i in startingitems:
            self.items.append(int(i))
        self.operationsign = operationsign
        self.operationconst = operationconst
        self.testdivisor = int(testdivisor)
        self.truecondition = int(truecondition)
        self.falsecondition = int(falsecondition)

    def additem(self, item):
        self.items.append(item)

    def printmonk(self):
        print(self.items)

    def movemonkp1(self):
        moves = []
        for i in self.items:
            curritemnew = None
            move = ''
            self.counttimes +=1
            if self.operationconst == 'old':
                if self.operationsign == "+":
                    curritemnew = i + i
                if self.operationsign == "*":
                    curritemnew = i * i

            else:
                if self.operationsign == "+":
                    curritemnew = i + int(self.operationconst)

                if self.operationsign == "*":
                    curritemnew = i * int(self.operationconst)
            curritemnew = int(curritemnew/3)
            move += str(curritemnew) + ' '
            if curritemnew % self.testdivisor == 0:
                move += str(self.truecondition)
            else:
                move += str(self.falsecondition)
            moves.append(move)
        self.items = []
        
        return moves
    
    
    def movemonkp2(self):
        moves = []
        for i in self.items:
            curritemnew = None
            move = ''
            self.counttimes +=1
            if self.operationconst == 'old':
                if self.operationsign == "+":
                    curritemnew = i + i
                if self.operationsign == "*":
                    curritemnew = i * i

            else:
                if self.operationsign == "+":
                    curritemnew = i + int(self.operationconst)

                if self.operationsign == "*":
                    curritemnew = i * int(self.operationconst)
            curritemnew = int(curritemnew) % 9699690
            move += str(curritemnew) + ' '
            if curritemnew % self.testdivisor == 0:
                move += str(self.truecondition)
            else:
                move += str(self.falsecondition)
            moves.append(move)
        self.items = []
        
        return moves
        

def createMonkeys(lineList):
    monkeys = []
    count = 0
    monkey = None
    startingitems = None
    operationsign = None
    operationconst = None
    testdivisor = None
    truecondition = None
    falsecondition = None

    for i in lineList:
        if count == 0:
            count +=1
        elif count == 1:
            count += 1
            splitstarting = i.split('Starting items: ')[1]
            startingitems = splitstarting.split(', ')
        elif count == 2:
            count +=1
            operationsplit = i.split(' ')
            operationsign = operationsplit[-2]
            operationconst = operationsplit[-1]
        elif count == 3:
            count += 1
            testdivisor = i.split(' ')[-1]
        elif count == 4:
            count +=1
            truecondition = i.split(' ')[-1]
        elif count == 5:
            count += 1
            falsecondition = i.split(' ')[-1]
        elif count == 6:
            monkey = Monkey(startingitems,operationsign,operationconst,testdivisor,truecondition,falsecondition)
            monkeys.append(monkey)
            count = 0

    return monkeys
    

def part1(lineList):
    monkeys = createMonkeys(lineList)
    for i in range(20):
        for j in monkeys:
            moves = j.movemonkp1()
            for k in moves:
                move = k.split(' ')
                monkeys[int(move[1])].additem(int(move[0]))
        pass

    counttimes = []

    for i in monkeys:
        counttimes.append(i.counttimes)
    counttimes.sort()
    return counttimes[-2] * counttimes[-1]

def part2(lineList):
    monkeys = createMonkeys(lineList)
    for i in range(10000):
        for j in monkeys:
            moves = j.movemonkp2()
            for k in moves:
                move = k.split(' ')
                monkeys[int(move[1])].additem(int(move[0]))
        pass

    counttimes = []

    for i in monkeys:
        counttimes.append(i.counttimes)
    counttimes.sort()
    return counttimes[-2] * counttimes[-1]

if __name__ == '__main__':
    lineList = readInput('../inputs/day11.txt')
    print(part1(lineList))
    print(part2(lineList))