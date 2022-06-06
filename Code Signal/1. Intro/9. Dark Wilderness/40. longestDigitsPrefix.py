#https://app.codesignal.com/arcade/intro/level-9/AACpNbZANCkhHWNs3

def solution(inputString):
    prefix = ""
    for i in inputString:
        try:
            a = int(i)
            prefix+=i
        except:
            break
    return prefix