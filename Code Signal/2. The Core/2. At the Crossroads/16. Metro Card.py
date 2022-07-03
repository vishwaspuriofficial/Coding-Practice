#https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/J7PQDxpWqhx7HrvBZ

def solution(lastNumberOfDays):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    possible = []

    for i in range(len(months)):
        if months[i] == lastNumberOfDays:
            a = i + 1
            if a == 12:
                a = 0
            print(a)
            if months[a] not in possible:
                possible.append(months[a])

    return possible