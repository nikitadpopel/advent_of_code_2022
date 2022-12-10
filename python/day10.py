import sys
sys.path.append('../')
from helper_functions import *
import time

                

def part1(lineList):
    cycles = 0
    register = 1
    cyclesvals = []
    for i in lineList:
        if i == 'noop':
            cycles +=1
            cyclesvals.append(register)
        else:
            splitval = i.split(' ')
            cycles +=1
            cyclesvals.append(register)
            cycles +=1
            register += int(splitval[1])
            cyclesvals.append(register)
    return (cyclesvals[18]*20) + (cyclesvals[58]*60) + (cyclesvals[98]*100) + (cyclesvals[138]*140) + (cyclesvals[178]*180) + (cyclesvals[218]*220)

def updateSprite(inputlocation):
    currentcrt = ''
    for i in range(0, 40):
        if i == inputlocation-1 or i == inputlocation or i == inputlocation + 1:
            currentcrt += '#'
        else:
            currentcrt += '.'
    return currentcrt

def checkcrt(inputlocation, sprite):
    mymodulo = inputlocation % 40
    if sprite[mymodulo] == "#":
        return '#'
    else:
        return '.'

def part2(lineList):
    cycles = 0
    register = 1
    cyclesvals = []
    currentcrt = '###.....................................'
    crtrow = ''
    crtrows = []
    for i in lineList:
        if i == 'noop':
            cycles +=1
            cyclesvals.append(register)
            if cycles == 41 or cycles == 81 or cycles == 121 or cycles == 161 or cycles == 201:
                crtrows.append(crtrow)
                crtrow = ''
            crtrow += checkcrt(cycles, currentcrt)
        else:
            splitval = i.split(' ')
            cycles +=1
            cyclesvals.append(register)
            if cycles == 41 or cycles == 81 or cycles == 121 or cycles == 161 or cycles == 201:
                crtrows.append(crtrow)
                crtrow = ''
            crtrow += checkcrt(cycles, currentcrt)
            cycles +=1
            register += int(splitval[1])
            currentcrt = updateSprite(register)
            cyclesvals.append(register)
            if cycles == 41 or cycles == 81 or cycles == 121 or cycles == 161 or cycles == 201:
                crtrows.append(crtrow)
                crtrow = ''
            crtrow += checkcrt(cycles, currentcrt)
    print(crtrows)
    for i in crtrows:
        print(i)
    print(crtrow)
    return (cyclesvals[18]*20) + (cyclesvals[58]*60) + (cyclesvals[98]*100) + (cyclesvals[138]*140) + (cyclesvals[178]*180) + (cyclesvals[218]*220)


if __name__ == '__main__':
    lineList = readInput('../inputs/day10.txt')
    print(part1(lineList))
    print(part2(lineList))