#https://app.codesignal.com/arcade/code-arcade/loop-tunnel/xzeZqCQjpfDJuN72S

def solution(param1, param2):
    ans = ""
    for i in range(1,len(str(max(param1,param2)))+1):
        try:
            ans+=str(int(str(param1)[-i])+int(str(param2)[-i]))[-1]
        except:
            try:
                ans+=str(int(str(param1)[-i]))
            except:
                ans+=str(int(str(param2)[-i]))
        print(ans)
    return int(ans[::-1])