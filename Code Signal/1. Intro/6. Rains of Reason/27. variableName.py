#https://app.codesignal.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno

def solution(name):
    # if name[0] == " ":
    #     return False
    try:
        numCheck = int(name[0])
        return False
    except:
        pass

    punctuation = " !#$%&'()*+, -./:;<=>?@[\]^`{|}~"
    for i in range(len(name)):
        if name[i] in punctuation:
            print(name[i])
            return False
    return True
