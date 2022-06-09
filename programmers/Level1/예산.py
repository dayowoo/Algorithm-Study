'''
- 최대한 많은 부서 > 낮은 금액부터 채워주기 :: 틀렸음
- 큰 수 부터 없앴어야 한다.
'''

# 왜 안될까 . . .
def solution(d, budget):
    count = 0
    min_value = min(d)
    while budget > min_value:
        min_value = min(d)
        budget -= min_value
        count += 1
        d.remove(min_value)
        print(d, min_value)
        
    return count




# 다른 풀이
'''
1. 리스트 정렬 : 낮은 수 -> 높은 수
2. 예산이 리스트합보다 작다면
3. 뒤의 요소(큰 수)부터 제거
4. 리스트 수 세기
'''
def solution2(d, budget):
    d.sort()
    print(d)
    while budget<sum(d):
        print(d, sum(d))
        d.pop()
        print(d)
        print("=======")
    return len(d)


print(solution2([1,3,2,5,4], 9))
