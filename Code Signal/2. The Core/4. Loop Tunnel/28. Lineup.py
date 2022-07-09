#https://app.codesignal.com/arcade/code-arcade/loop-tunnel/8rqs3BLpdKePhouQM

def solution(commands):
    a = 0
    b = 0
    count = 0
    for i in commands:
        if i == "L":
            a -= 90
            b += 90
        elif i == "R":
            a += 90
            b -= 90
        else:
            a += 180
            b += 180

        print(i, a, b)
        if (a >= 360):
            a -= 360
        elif (a <= -360):
            a += 360
        if (b >= 360):
            b -= 360
        elif (b <= -360):
            b += 360

        if a + 360 == b or b + 360 == a or a == b:
            print("+1")
            count += 1

    return count