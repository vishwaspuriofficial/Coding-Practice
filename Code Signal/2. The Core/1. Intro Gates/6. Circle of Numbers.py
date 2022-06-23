#https://app.codesignal.com/arcade/code-arcade/intro-gates/vExYvcGnFsEYSt8nQ

def solution(n, firstNumber):
    a = []

    for i in range(n):
        a.append(i)

    while a[0] != firstNumber:
        a.append(a[0])
        a.pop(0)

    return a[(n // 2)]