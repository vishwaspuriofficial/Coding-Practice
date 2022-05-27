#https://app.codesignal.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui

def solution(inputString):
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    new = ""

    for i in inputString:
        a = alphabets.index(i) + 1
        if a >= 26:
            a -= 26
        print(a)
        new += alphabets[a]

    return new