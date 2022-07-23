#https://app.codesignal.com/arcade/code-arcade/list-forest-edge/3LmZafR9wMCWpdgra

def solution(arr):
    l = len(arr)
    if l % 2 == 0:
        median = sum(arr[l // 2 - 1:l // 2 + 1])
    else:
        median = arr[l // 2]

    print(median)
    return True if median == arr[0] == arr[-1] else False