#https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/7jaup9HprdJno2diw

def solution(score1, score2):
    return True if (score1 == 6 and score2 < 5) or (score2 == 6 and score1 < 5) or (score1>=5 and score1<7 and score2 == 7) or (score1==7 and score2 >= 5 and score2<7) else False