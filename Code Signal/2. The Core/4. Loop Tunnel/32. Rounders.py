#https://app.codesignal.com/arcade/code-arcade/loop-tunnel/H5PP5MXvYvWXxTytH

def solution(n):
    print(n)
    if type(n) == int:
        n = str(n)

    n = list(n)

    if n.count(0) == len(n) - 1:
        n = "".join(str(e) for e in n)
        return int(n)

    for i in range(1, len(n)):
        if int(n[-i]) != 0:
            print(int(n[-i]))
            if int(n[-i]) >= 5:
                n[-i] = 0
                n[-(i + 1)] = int(n[-(i + 1)]) + 1
            else:
                n[-i] = 0
            solution(n)
    n = "".join(str(e) for e in n)
    return int(n)