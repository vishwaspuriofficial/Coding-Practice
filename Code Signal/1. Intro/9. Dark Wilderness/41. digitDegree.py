#https://app.codesignal.com/arcade/intro/level-9/hoLtYWbjdrD2PF6yo

def solution(n):
    def sumOf(n):
        a = 0
        for i in n:
            a += int(i)

        return str(a)

    count = 0
    n = str(n)
    while len(n) != 1:
        n = sumOf(n)
        count += 1
    return count