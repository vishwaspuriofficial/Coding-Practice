#https://app.codesignal.com/arcade/intro/level-11/vpfeqDwGZSzYNm2uX

def solution(n):
    m = 0
    n = str(n)
    for i in range(len(n)):
        a = int(n[:i] + n[i + 1:])
        if a > m:
            m = a

    return m