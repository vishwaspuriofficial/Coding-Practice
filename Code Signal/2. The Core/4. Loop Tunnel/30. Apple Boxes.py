#https://app.codesignal.com/arcade/code-arcade/loop-tunnel/scG8AFsPuqQGx8Qjf

def solution(k):
    r = 0
    y = 0

    for i in range(1, k + 1):
        if i % 2 == 0:
            r += i ** 2
        else:
            y += i ** 2
    return r - y