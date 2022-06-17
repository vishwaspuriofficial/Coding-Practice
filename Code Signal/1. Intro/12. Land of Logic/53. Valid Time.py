#https://app.codesignal.com/arcade/intro/level-12/ywMyCTspqGXPWRZx5

def solution(time):
    return True if int(time.split(":")[0])>=0 and int(time.split(":")[0])<24 and int(time.split(":")[1])>=0 and int(time.split(":")[1])<60 else False