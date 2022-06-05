#https://app.codesignal.com/arcade/intro/level-8/8N7p3MqzGQg5vFJfZ

def solution(s):
    lets = []
    for i in s:
        if i not in lets:
            lets.append(i)

    return len(lets)