#https://app.codesignal.com/arcade/intro/level-7/ZFnQkq9RmMiyE6qtq

def solution(a):
    sums = []

    for i in range(len(a)):
        count = 0
        for j in range(len(a)):
            count += abs(a[i] - a[j])
        sums.append(count)

    return a[sums.index(min(sums))]