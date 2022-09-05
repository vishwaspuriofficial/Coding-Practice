#https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/pdw3izd7SpMTBJqSy

def solution(current, numberOfDigits):
    numberOfDigits -= len(str(current))
    while numberOfDigits >= len(str(current)):
        current += 1
        numberOfDigits -= len(str(current))
        print(current)

    return current