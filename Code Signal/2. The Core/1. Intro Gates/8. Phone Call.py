#https://app.codesignal.com/arcade/code-arcade/intro-gates/mZAucMXhNMmT7JWta

def solution(min1, min2_10, min11, s):
    prices = [min1, min2_10, min2_10, min2_10, min2_10, min2_10, min2_10, min2_10, min2_10, min2_10, min11]

    i = 0
    mins = 0
    while s - prices[0] >= 0:
        s -= prices[i]
        mins += 1
        if len(prices) == 1:
            continue
        prices.pop(0)
        print(s, mins)
    return mins