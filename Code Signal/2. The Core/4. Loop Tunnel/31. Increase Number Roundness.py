#https://app.codesignal.com/arcade/code-arcade/loop-tunnel/KLbRMcWhaZi3dvYH5

def solution(n):
    n = str(n)
    for i in range(1, len(n)):
        if n[-i] != "0":
            if n[-i - 1] == "0":
                return True

    return False