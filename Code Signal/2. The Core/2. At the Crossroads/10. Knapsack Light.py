#https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/r9azLYp2BDZPyzaG2

def solution(value1, weight1, value2, weight2, maxW):
    if value1>value2 and weight1<maxW:
        if weight1+weight2<=maxW:
            return value1+value2
        return value1
    else:
        if weight2<=maxW:
            return value2
        elif weight1<=maxW:
            return value1
    return 0