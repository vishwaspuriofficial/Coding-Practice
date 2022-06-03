#https://app.codesignal.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R

def solution(inputArray, k):
    a = 1
    step = 0
    while step + k <= len(inputArray):
        step += k - 1

        inputArray.pop(step)
        print(step, inputArray)
        # a+=1

    return inputArray
