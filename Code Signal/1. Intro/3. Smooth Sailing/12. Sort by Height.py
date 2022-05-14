#https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

def solution(a):
    people = []
    points = []
    for i in range(len(a)):
        if a[i] != -1:
            people.append(a[i])
            points.append(i)
    people.sort()
    print(people, points)

    for i in range(len(points)):
        a[points[i]] = people[i]

    return a