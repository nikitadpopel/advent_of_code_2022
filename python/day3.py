def readInput(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def part1(lineList):
    pass


def part2(lineList):
    pass

if __name__ == '__main__':
    lineList = readInput('day3.txt')
    print(lineList)
    print(part1(lineList))
    print(part2(lineList))