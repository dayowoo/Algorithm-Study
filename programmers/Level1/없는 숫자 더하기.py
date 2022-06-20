

def solution(numbers):
    num_list = [i for i in range(0,10)]
    answer = set(num_list) - set(numbers)
    
    return sum(answer)

print(solution([1,2,3,4,6,7,8,0]))


# 다른 풀이
def solution2(numbers):
    return 45 - sum(numbers)


def solution3(numbers):
    return sum([i for i in [1,2,3,4,5,6,7,8,9,0] if i not in numbers])