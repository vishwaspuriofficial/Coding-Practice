#https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9

def solution(a):
    b = 0
    c = 0
    for i in range(len(a)):
        if i % 2 == 0:
            b += a[i]
        else:
            c += a[i]

    return [b, c]