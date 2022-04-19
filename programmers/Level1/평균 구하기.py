'''
1. 리스트 원소 개수 구하기 : len(arr)
2. 리스트 합 구하기 : sum(arr)
'''


def avgList(arr):
    answer = sum(arr)/len(arr)
    return answer

print(avgList([1,2,3,4]))