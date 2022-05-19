#https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg

def solution(inputArray):
    count = 0
    for i in range(1,len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            count += abs(inputArray[i]-inputArray[i-1])+1
            inputArray[i] += abs(inputArray[i]-inputArray[i-1])+1
    return count