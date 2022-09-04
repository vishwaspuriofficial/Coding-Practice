#https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/MvX84CA5HN6GKqv7R

def solution(a0):
    appeared = [a0]
    ins = 1
    while (appeared[-1]**2 not in appeared):
        ins+=1
        a = 0
        for j in str(appeared[-1]):
           a += int(j)**2
        appeared.append(a)
        if appeared.count(a) > 1:
            return ins
        print(appeared)
    return ins+1