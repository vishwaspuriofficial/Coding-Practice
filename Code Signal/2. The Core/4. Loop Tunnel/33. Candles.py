#https://app.codesignal.com/arcade/code-arcade/loop-tunnel/LAKReA3CR9EwkZGSz

def solution(candlesNumber, makeNew):
    ans = [candlesNumber]
    rem = candlesNumber

    while rem >= makeNew:
        ans.append(rem // makeNew)
        rem = rem % makeNew + ans[-1]

    return sum(ans)