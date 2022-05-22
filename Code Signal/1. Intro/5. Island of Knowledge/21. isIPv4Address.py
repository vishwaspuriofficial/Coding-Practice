#https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso

def solution(inputString):
    inputString = inputString.split(".")
    if len(inputString) == 4:
        for i in inputString:
            try:
                if int(i) >= 0 and int(i) < 256:
                    if len(i) > 1 and i[0] == "0" and int(i[1]) >= 0:
                        return False
                else:
                    return False
            except:
                return False
    else:
        return False

    return True