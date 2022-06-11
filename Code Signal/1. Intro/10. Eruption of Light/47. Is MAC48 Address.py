#https://app.codesignal.com/arcade/intro/level-10/HJ2thsvjL25iCvvdm

def solution(inputString):
    lets = "ABCDEF"

    inputString = inputString.split("-")

    if len(inputString) != 6:
        return False

    for i in inputString:
        if len(i) != 2:
            return False

        for j in i:
            try:
                if not int(j) >= 0 and int(j) <= 9:
                    return False

            except:
                if j not in lets:
                    return False

    return True

    # if letter a-f
    # num 0-9
    # len split == 6
    # len of each == 2