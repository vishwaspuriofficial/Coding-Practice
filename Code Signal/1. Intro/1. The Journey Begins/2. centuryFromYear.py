# https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN

def solution(year):
    a = year // 100
    if a*100 == year:
        return a
    else:
        return a+1
