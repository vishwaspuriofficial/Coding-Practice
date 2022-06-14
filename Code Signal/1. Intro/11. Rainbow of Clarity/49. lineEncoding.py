#https://app.codesignal.com/arcade/intro/level-11/o2uq6eTuvk7atGadR

def solution(s):
    substrings = []
    a = 0
    b = ""
    while a < len(s):
        if s[a] in b or b == "":
            b += s[a]
        else:
            substrings.append(b)
            b = s[a]
        a += 1
    substrings.append(b)
    print(substrings)
    new = ""
    for i in substrings:
        if len(i) == 1:
            new += i
        else:
            new += str(len(i))
            new += i[0]

    return new