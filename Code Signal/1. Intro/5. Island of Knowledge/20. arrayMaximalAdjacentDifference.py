#https://app.codesignal.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE

def solution(inputArray):
    m = abs(inputArray[0] - inputArray[1])

    for i in range(1, len(inputArray)):
        if abs(inputArray[i] - inputArray[i - 1]) > m:
            m = abs(inputArray[i] - inputArray[i - 1])

    return m