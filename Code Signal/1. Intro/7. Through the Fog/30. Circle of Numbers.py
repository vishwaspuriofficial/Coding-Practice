#https://app.codesignal.com/arcade/intro/level-7/vExYvcGnFsEYSt8nQ

def solution(n, firstNumber):
    a = []
    for i in range(n):
        a.append(i)

    while a[0] != firstNumber:
        a.append(a[0])
        a.pop(0)

    return a[len(a) // 2]