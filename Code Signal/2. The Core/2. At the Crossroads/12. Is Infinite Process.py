#https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/aFF9HDm2Rsti9j5kc

def solution(a, b):
    while a!=b:
        if a>b:
            return True
        a+=1
        b-=1
    return False