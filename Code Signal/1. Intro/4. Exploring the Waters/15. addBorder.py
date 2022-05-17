#https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN

def solution(picture):
    for i in range(len(picture)):
        picture[i] = "*" + picture[i] + "*"
    a = len(picture[0])

    picture.insert(0, "*" * a)
    picture.append("*" * a)
    return picture