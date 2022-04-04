#https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m

def solution(inputArray):
    m = inputArray[0] * inputArray[1]
    for i in range(len(inputArray) - 1):
        if inputArray[i] * inputArray[i + 1] > m:
            m = inputArray[i] * inputArray[i + 1]

    return m
