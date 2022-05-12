#https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

def solution(s1, s2):
    common = 0
    s2 = list(s2)
    for i in s1:
        if i in s2:
            common += 1
            s2.pop(s2.index(i))

    return common