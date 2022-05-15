#https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6

def solution(inputString):
    inputString = list(inputString)
    new = ""
    a = 0
    b = 0
    while "(" in inputString:
        for i in range(len(inputString)):
            if inputString[i] == "(":
                a = i
            elif inputString[i] == ")":
                b = i
                break

        inputString[a:b + 1] = inputString[a + 1:b][::-1]

    return "".join(str(e) for e in inputString)