def readInput(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def getScore(hand):
    if hand == 'X':
        return 1
    elif hand == 'Y':
        return 2
    elif hand == 'Z':
        return 3
    else:
        return 0

def part1(lineList):
    score = 0
    for i in lineList:
        hands = i.split(' ')

        if (hands[0] == 'A' and hands[1] == 'X') or (hands[0] == 'B' and hands[1] == 'Y')or (hands[0] == 'C' and hands[1] == 'Z'):
            score += 3 + getScore(hands[1])
        if (hands[0] == 'A' and hands[1] == 'Z') or (hands[0] == 'B' and hands[1] == 'X')or (hands[0] == 'C' and hands[1] == 'Y'):
            score += 0 + getScore(hands[1])
        if (hands[0] == 'A' and hands[1] == 'Y') or (hands[0] == 'B' and hands[1] == 'Z')or (hands[0] == 'C' and hands[1] == 'X'):
            score += 6 + getScore(hands[1])
    return score


def part2(lineList):
    score = 0
    for i in lineList:
        hands = i.split(' ')
        if hands[1] == 'X':
            if hands[0] == 'A':
                score += getScore('Z')
            if hands[0] == 'B':
                score += getScore('X')
            if hands[0] == 'C':
                score += getScore('Y')
        if hands[1] == 'Y':
            if hands[0] == 'A':
                score += 3 + getScore('X')
            if hands[0] == 'B':
                score += 3 + getScore('Y')
            if hands[0] == 'C':
                score += 3 + getScore('Z')

        if hands[1] == 'Z':
            if hands[0] == 'A':
                score += 6 + getScore('Y')
            if hands[0] == 'B':
                score += 6 + getScore('Z')
            if hands[0] == 'C':
                score += 6 + getScore('X')

    return score

if __name__ == '__main__':
    lineList = readInput('day2.txt')
    print(part1(lineList))
    print(part2(lineList))