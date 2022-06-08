#https://app.codesignal.com/arcade/intro/level-10/PHSQhLEw3K2CmhhXE

def solution(inputString):
    lengths = {}
    for i in inputString:
        if i in lengths:
            lengths[i] += 1
        else:
            lengths[i] = 1

    letters = sorted(list(lengths.keys()))

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in range(alphabets.index(letters[-1]) + 1):
        if alphabets[i] not in letters:
            lengths[alphabets[i]] = 0
            letters = sorted(list(lengths.keys()))

    print(letters, lengths)
    for j in range(len(letters) - 1):
        print(letters[j], lengths[letters[j]], lengths[letters[j + 1]])
        if lengths[letters[j]] < lengths[letters[j + 1]]:
            return False
    return True