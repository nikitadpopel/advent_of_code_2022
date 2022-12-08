import sys
sys.path.append('../')
from helper_functions import *
import time

def getOuterSize(lineList):
    height = len(lineList) - 2
    width = len(lineList[0])
    outersize = (height * 2) + (width * 2)
    return outersize

def part1(lineList):
    visiblecount = getOuterSize(lineList)
    
    for i in range(1, len(lineList)-1):
        for j in range(1, len(lineList[i])-1):
            isvisible = False
            isvisibleleft = True
            isvisibleright = True
            isvisibletop= True
            isvisiblebottom = True
            # left check
            for k in range(0, j):
                if lineList[i][j] <= lineList[i][k]:
                    isvisibleleft = False

            # right check
            for k in range(j+1, len(lineList)):
                if lineList[i][j] <= lineList[i][k]:
                    isvisibleright = False

            # top check
            for k in range(0, i):
                if lineList[i][j] <= lineList[k][j]:
                    isvisibletop = False

            # bottom check
            for k in range(i+1, len(lineList[i])):
                if lineList[i][j] <= lineList[k][j]:
                    isvisiblebottom = False

            if isvisibletop or isvisiblebottom or isvisibleleft or isvisibleright:
                isvisible = True
                visiblecount += 1
    
    return visiblecount

def part2(lineList):
    visiblecount = getOuterSize(lineList)
    
    treescores = []

    for i in range(0, len(lineList)):
        for j in range(0, len(lineList[i])):
            isvisible = False
            checkingleft = True
            checkingright = True
            checkingtop= True
            checkingbottom = True
            leftcount = 0
            rightcount = 0
            topcount = 0
            bottomcount = 0
            # left check
            while(checkingleft):
                if j == 0:
                    checkingleft = False
                for k in range(0, j):
                    leftcount += 1
                    
                    if lineList[i][j] <= lineList[i][j-k-1]:
                        checkingleft = False
                        break
                    checkingleft = False

            # right check
            while(checkingright):
                if j == len(lineList) - 1:
                    checkingright = False
                for k in range(j+1, len(lineList)):
                    rightcount += 1
                    if lineList[i][j] <= lineList[i][k]:
                        checkingright = False
                        break
                    checkingright = False

            # top check
            while(checkingtop):
                if i == 0:
                    checkingtop = False
                for k in range(0, i):
                    topcount += 1
                    if lineList[i][j] <= lineList[i-k-1][j]:
                        checkingtop = False
                        break
                    checkingtop = False

            # bottom check
            while(checkingbottom):
                if i == len(lineList[i]) - 1:
                    checkingbottom = False
                for k in range(i+1, len(lineList[i])):
                    bottomcount += 1
                    
                    if lineList[i][j] <= lineList[k][j]:
                        checkingbottom = False
                        break
                    checkingbottom = False
            thisscore = topcount * leftcount * bottomcount * rightcount
            treescores.append(thisscore)

    return max(treescores)

if __name__ == '__main__':
    lineList = readInput('../inputs/day8.txt')
    print(part1(lineList))
    print(part2(lineList))