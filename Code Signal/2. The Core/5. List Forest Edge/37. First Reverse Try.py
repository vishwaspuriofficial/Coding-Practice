#https://app.codesignal.com/arcade/code-arcade/list-forest-edge/ND8nghbndTNKPP4Tb

def solution(arr):
    if len(arr) == 0:
        return []
    arr[0],arr[-1] = arr[-1],arr[0]
    return arr