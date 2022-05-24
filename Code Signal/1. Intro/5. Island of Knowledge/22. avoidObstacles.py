#https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5

def solution(inputArray):
    a = 0
    b = 1
    while a <= max(inputArray):
        if a in inputArray:
            b += 1
            a = 0

        else:
            a += b
    return b