#https://app.codesignal.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi

def solution(cell1, cell2):
    lets = " ABCDEFGH"

    def black(cell):
        if lets.index(cell[0]) % 2 == 0 and int(cell[1]) % 2 == 0:
            return True
        if lets.index(cell[0]) % 2 != 0 and int(cell[1]) % 2 != 0:
            return True
        return False

    if black(cell1) == black(cell2):
        return True
    return False