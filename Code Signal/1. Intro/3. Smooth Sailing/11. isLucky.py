#https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

def solution(n):
    n = list(map(int, str(n)))
    return True if sum(n[:(len(n)//2)]) == sum(n[(len(n)//2):]) else False