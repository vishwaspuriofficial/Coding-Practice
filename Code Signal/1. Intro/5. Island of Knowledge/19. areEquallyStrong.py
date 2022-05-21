#https://app.codesignal.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return True if yourLeft == friendsLeft and yourRight == friendsRight or yourLeft == friendsRight and yourRight == friendsLeft else False