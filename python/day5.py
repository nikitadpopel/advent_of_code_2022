import sys
sys.path.append('../')
from helper_functions import *

def setupStacks(lines):
    # for i in lines:
    stacks = {}
    stackamount = int(lines[-1][-1])
    for i in range(stackamount):
        stacks[i] = []
    for i in range(len(lines)-1):
        currline = lines[len(lines)-2 - i]
        myrange = [1,5,9,13,17,21,25,29, 33]
        for x,j in enumerate(currline):
            if x in myrange:
                stacks[(x-1)/4].append(j)
    for i in range(stackamount):
        while(' ' in stacks[i]):
            stacks[i].remove(' ')
    return stacks

def setupCommands(lines):
    commands = []
    for i in lines:
        
        rawcommand = i.split(' ')
        command = [int(rawcommand[1]), int(rawcommand[3]), int(rawcommand[5])]
        commands.append(command)
    return commands

def part1(lineList):
    index = 0
    for i in lineList:
        if i == '':
            break
        index+=1

    stacks = setupStacks(lineList[:index])
    commands = setupCommands(lineList[index+1:])
    for i in commands:
        for j in range(i[0]):
            stacks[i[2]-1].append(stacks[i[1]-1].pop())

    topcratestr = ''
    for i in stacks.values():
        topcratestr += i[-1]
    return topcratestr

def part2(lineList):
    index = 0
    for i in lineList:
        if i == '':
            break
        index+=1

    stacks = setupStacks(lineList[:index])
    commands = setupCommands(lineList[index+1:])
    
    for i in commands:
        oldstack = stacks[i[1]-1]
        stacklength = len(oldstack)
        stacks[i[2]-1] += oldstack[stacklength-i[0]:stacklength]
        for j in range(i[0]):
            stacks[i[1]-1].pop()
    topcratestr = ''
    for i in stacks.values():
        topcratestr += i[-1]
    return topcratestr

if __name__ == '__main__':
    lineList = readInput('../inputs/day5.txt')
    print(part1(lineList))
    print(part2(lineList))