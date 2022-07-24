#https://app.codesignal.com/arcade/code-arcade/list-forest-edge/APD5T5CybxTtfkdjL

def solution(arr):
    l = len(arr)
    if l%2==0:
        m = sum(arr[l//2-1:l//2+1])
        x = []
        for i in arr[:l//2-1]:
            x.append(i)
        x.append(m)
        for j in arr[l//2+1:]:
            x.append(j)
        return x
    else:
        return arr