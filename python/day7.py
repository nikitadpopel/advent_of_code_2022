import sys
sys.path.append('../')
from helper_functions import *

def moveUpDir(mystr):
    returndir = ''
    tempstrlist = mystr.split('/')
    while tempstrlist.count('') > 0:
        tempstrlist.remove('')
    for i in range(0, len(tempstrlist)-1):
        returndir += '/' +tempstrlist[i]
    returndir += '/'
    return returndir

def getDirectoryValue(directoryname, files, filesize):
    size = 0
    for i in files:
        if i.find(directoryname) != -1:
            size += filesize[i]
    return size

def getMyStuff(lineList):
    files = []
    currdir = '/'
    filesize = {}
    directories = []

    for i in lineList[1:]:
        tempsplit = i.split(' ')
        if tempsplit[0] == '$' and tempsplit[1] == 'cd':
            if tempsplit[-1] == '..':
                currdir = moveUpDir(currdir)
            elif tempsplit[-1] == '/':
                currdir = '/'
            else:
                currdir += tempsplit[-1] + '/'
        elif tempsplit[0] == '$' and tempsplit[1] == 'ls':
            pass
        else:
            if tempsplit[0] == 'dir':
                newdirlocation = currdir + tempsplit[1] + '/'
                directories.append(newdirlocation)
            else:
                newfile = currdir + tempsplit[1]
                files.append(newfile)
                filesize[newfile] = int(tempsplit[0])
    return files, filesize, directories

def part1(lineList):
    
    files,filesize,directories = getMyStuff(lineList)

    part1return = 0

    for i in directories:
        thisdirsize = getDirectoryValue(i, files, filesize)
        if thisdirsize <= 100000:
            part1return += thisdirsize 
    return part1return

def part2(lineList):
    
    files,filesize,directories = getMyStuff(lineList)

    part1return = 0
    spaceleft = 70000000 - (getDirectoryValue('/', files, filesize))
    possibledellist = []
    for i in directories:
        thisdirsize = getDirectoryValue(i, files, filesize)
        hypotheticalsize = thisdirsize + spaceleft
        if hypotheticalsize > 30000000:
            possibledellist.append(thisdirsize)
    return min(possibledellist)

if __name__ == '__main__':
    lineList = readInput('../inputs/day7.txt')
    print(part1(lineList))
    print(part2(lineList))