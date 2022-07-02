#https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/jZ4ZSiGohzFTeg4yb

def solution(young, beautiful, loved):
    if (young and beautiful and not loved):
        print("A")
    elif (loved and not young or not beautiful):
        print("B")
    else:
        print("C")
    return True if (young==True and beautiful==True and loved==False) or (loved==True and (young==False or beautiful==False)) else False