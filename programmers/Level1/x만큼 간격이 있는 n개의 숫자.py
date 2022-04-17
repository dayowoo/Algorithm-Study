def solution(x, n):
    answer = []
    answer.append(x)
    for i in range(n-1):
        y = answer[i]+x
        answer.append(y)
    return answer

print(solution(2, 5))