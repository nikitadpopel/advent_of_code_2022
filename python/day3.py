def readInput(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def getScore(letter):
    alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet.find(letter)

def part1(lineList):
    score = 0
    for i in lineList:
        divisor = int(len(i)/2)
        temp1 = i[:divisor]
        temp2 = i[divisor:]
        letter = ''
        for i in temp1:
            for j in temp2:
                if i == j:
                    letter = i

        score += getScore(letter)
    return score

def part2(lineList):
    score = 0
    for i in range(100):
        for x_i in lineList[(i*3)]:
            for x_j in lineList[(i*3)+1]:
                for x_k in lineList[(i*3)+2]:
                    if x_i == x_j and x_i == x_k:
                        letter = x_i
        score += getScore(letter)
    return score

if __name__ == '__main__':
    lineList = readInput('day3.txt')
    print(part1(lineList))
    print(part2(lineList))