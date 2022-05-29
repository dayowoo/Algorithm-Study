'''
1. 1~n까지 n을 나눔
2. 

- /, %, divmod
'''

def solution(n):
    answer = []
    i = 1
    while True:
        if n==0:
            return 0
        if n%i==0:
            answer.append(i)
        i +=1
        if i > n:
            break
    return sum(answer)


print(solution(0))