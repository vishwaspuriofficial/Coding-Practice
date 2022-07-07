#https://app.codesignal.com/arcade/code-arcade/loop-tunnel/LbuWRHnMoJH9SAo4o

def solution(a, b, n):
    if n == 1:
        return a * b
    return solution(a + 1, b + 1, n - 1)