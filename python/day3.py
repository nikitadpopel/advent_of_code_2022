def readInput(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def getScore(letter):
    if letter == 'a':
        return 1
    if letter == 'b':
        return 2
    if letter == 'c':
        return 3
    if letter == 'd':
        return 4
    if letter == 'e':
        return 5
    if letter == 'f':
        return 6
    if letter == 'g':
        return 7
    if letter == 'h':
        return 8
    if letter == 'i':
        return 9
    if letter == 'j':
        return 10
    if letter == 'k':
        return 11
    if letter == 'l':
        return 12
    if letter == 'm':
        return 13
    if letter == 'n':
        return 14
    if letter == 'o':
        return 15
    if letter == 'p':
        return 16
    if letter == 'q':
        return 17
    if letter == 'r':
        return 18
    if letter == 's':
        return 19
    if letter == 't':
        return 20
    if letter == 'u':
        return 21
    if letter == 'v':
        return 22
    if letter == 'w':
        return 23
    if letter == 'x':
        return 24
    if letter == 'y':
        return 25
    if letter == 'z':
        return 26
    if letter == 'A':
        return 27
    if letter == 'B':
        return 28
    if letter == 'C':
        return 29
    if letter == 'D':
        return 30
    if letter == 'E':
        return 31
    if letter == 'F':
        return 32
    if letter == 'G':
        return 33
    if letter == 'H':
        return 34
    if letter == 'I':
        return 35
    if letter == 'J':
        return 36
    if letter == 'K':
        return 37
    if letter == 'L':
        return 38
    if letter == 'M':
        return 39
    if letter == 'N':
        return 40
    if letter == 'O':
        return 41
    if letter == 'P':
        return 42
    if letter == 'Q':
        return 43
    if letter == 'R':
        return 44
    if letter == 'S':
        return 45
    if letter == 'T':
        return 46
    if letter == 'U':
        return 47
    if letter == 'V':
        return 48
    if letter == 'W':
        return 49
    if letter == 'X':
        return 50
    if letter == 'Y':
        return 51
    if letter == 'Z':
        return 52

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