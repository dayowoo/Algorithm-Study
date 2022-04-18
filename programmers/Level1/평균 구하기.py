'''
1. 리스트 원소 개수 구하기 : len(arr)
2. 리스트 합 구하기 : sum(arr)
'''


def solution(arr):
    print(len(arr))
    print(sum(arr))
    answer = sum(arr)/len(arr)
    return answer

print(solution([1,2,3,4]))