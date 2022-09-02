#https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/yBFfNv5fTqhcacZ7w

import math
def solution(n):
    for i in range(int(math.sqrt(n))+1):
        for j in range(i+1):
            if i**j == n:
                return True
    return False