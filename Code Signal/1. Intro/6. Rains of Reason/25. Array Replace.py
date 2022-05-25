#https://app.codesignal.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm

def solution(a):
    def solution(inputArray, elemToReplace, substitutionElem):
        for i in range(len(inputArray)):
            if inputArray[i] == elemToReplace:
                inputArray[i] = substitutionElem

        return inputArray