'''
1.
2. 빈 배열인지 판단하기

'''


def solution(arr):
    if not arr:  # len(answer)==0
        return [-1]
    else:
        arr.remove(min(arr))
        return arr


print(solution([4,3,2,1]))