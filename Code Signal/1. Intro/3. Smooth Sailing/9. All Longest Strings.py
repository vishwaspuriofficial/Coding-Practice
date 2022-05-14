#https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

def solution(inputArray):
    longest = 0
    for i in inputArray:
        if len(i) > longest:
            longest = len(i)
    longestStrings = []
    for j in inputArray:
        if len(j) == longest:
            longestStrings.append(j)

    return longestStrings
