#https://app.codesignal.com/arcade/code-arcade/loop-tunnel/hBw5BJiZ4LmXcy92u

def solution(n, l, r):
    count = 0
    for i in range(l, (n // 2) + 1):
        print(i)
        if n - i <= r:
            count += 1

    return count