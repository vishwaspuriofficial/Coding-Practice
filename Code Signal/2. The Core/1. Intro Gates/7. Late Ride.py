#https://app.codesignal.com/arcade/code-arcade/intro-gates/aiKck9MwwAKyF8D4L

def solution(n):
    h = n//60
    m = n%60
    t = str(h)+str(m)
    return sum(map(int, t))