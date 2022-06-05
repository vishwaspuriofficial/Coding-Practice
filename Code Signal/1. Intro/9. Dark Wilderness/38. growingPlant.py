#https://app.codesignal.com/arcade/intro/level-9/xHvruDnQCx7mYom3T

def solution(upSpeed, downSpeed, desiredHeight):
    h = 0
    days = 0
    while h+(upSpeed-downSpeed)<desiredHeight:
        days+=1
        h+=upSpeed
        if h>=desiredHeight:
            return days
        h-=downSpeed
    return days
