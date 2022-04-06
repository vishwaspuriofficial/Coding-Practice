#https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

def solution(n):
    if n==1:
        return 1
    return (n*n) + ((n-1)**2)