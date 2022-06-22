#https://app.codesignal.com/arcade/code-arcade/intro-gates/HEsmEacHr2s9wahjr

def solution(divisor, bound):
    i = bound
    while i>=0 and i%divisor!=0:
        i-=1
    return i