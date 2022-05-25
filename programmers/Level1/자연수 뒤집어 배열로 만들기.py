'''
sort(reverse=True) 와 reverse()의 차이

- 둘다 리스트 메소드
- sort()는 기준에 따라 오름차순, 내림차순 정렬을 하는 것
- reverse()는 단순히 리스트의 순서를 뒤집는 것



'''

def solution(n):
    nList = list(str(n))    # ['1','2' ...]
    intList = list(map(int, nList))     # [int(x) for x in nList]
    intList.reverse()
    return intList

print(solution(5000))