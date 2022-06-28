#https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/sgDWKCFQHHi5D3Szj

def solution(a, b, c):
    d = [a,b,c]
    for i in d:
        if d.count(i)==1:
            return i