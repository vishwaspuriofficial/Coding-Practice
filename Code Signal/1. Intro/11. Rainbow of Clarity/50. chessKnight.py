#https://app.codesignal.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb

def solution(cell):
    let = "abcdefgh"
    x = let.index(cell[0])
    y = int(cell[1]) - 1
    print(x, y)
    count = 0
    possibilities = [[1, 2], [-1, 2], [2, 1], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

    for a, b in possibilities:
        if x + a >= 0 and x + a < 8 and y + b >= 0 and y + b < 8:
            print(x + a, y + b)
            count += 1

    return count