#https://app.codesignal.com/arcade/code-arcade/list-forest-edge/bq2XnSr5kbHqpHGJC

def solution(statues):
    count = 0
    for i in range(min(statues), max(statues)):
        if i not in statues:
            count += 1

    return count