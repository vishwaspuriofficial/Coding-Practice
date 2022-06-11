#https://app.codesignal.com/arcade/intro/level-10/8RiRRM3yvbuAd3MNg

def solution(votes, k):
    count = 0
    highest = max(votes)
    if k == 0 and votes.count(highest) == 1:
        return 1
    for i in votes:
        if k + i > highest:
            count += 1

    return count