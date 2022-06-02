

def solution(numbers):
    a = [x for x in range(0,10)]
    sub = [x for x in a if x not in numbers]
    return sum(sub)


print(solution([1,2,3,4,6,7,8,0]))