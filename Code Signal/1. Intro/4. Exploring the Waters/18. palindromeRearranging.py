#https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico

def solution(inputString):
    a = []

    for i in inputString:
        if i in a:
            a.remove(i)
        else:
            a.append(i)

    if len(inputString) % 2 == 0 and len(a) == 0 or len(inputString) % 2 == 1 and len(a) == 1:
        return True
    return False