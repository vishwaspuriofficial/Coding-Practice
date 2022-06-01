#https://app.codesignal.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb

def solution(deposit, rate, threshold):
    count = 0
    while deposit < threshold:
        count += 1
        deposit += deposit * (rate / 100)

    return count