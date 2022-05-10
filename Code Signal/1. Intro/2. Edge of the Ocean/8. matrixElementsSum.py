#https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
def solution(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0:
                for i in range(row):
                    if matrix[i][col] == 0:
                        break
                else:
                    count+=matrix[row][col]
    return count