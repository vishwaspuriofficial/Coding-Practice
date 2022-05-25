#https://app.codesignal.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW

def solution(n):
    n= str(n)
    for i in str(n):
        if int(i)%2 !=0:
            return False
    return True