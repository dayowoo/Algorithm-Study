'''
원리 : 2/N 과 포켓몬의 종류 중 더 낮은 수를 return
'''

def solution(nums):
    divide = len(nums)/2
    set_nums = len(set(nums))
    if set_nums >= divide:
        answer = divide
    elif divide > set_nums:
        answer = set_nums
    return answer


# 다른 풀이
def solution2(ls):
    return min(len(ls)/2, len(set(ls)))


print(solution([3,1,2,3]))