#https://app.codesignal.com/arcade/code-arcade/loop-tunnel/7BFPq6TpsNjzgcpXy

def solution(n):
    count = 1
    i = 1
    while count < n:
        count *= i
        i += 1
    return count