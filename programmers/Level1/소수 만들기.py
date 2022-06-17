'''
- 3개의 수를 조합해서 만든다 : permutations, combinations

-

'''

# 순열
'''
from itertools import permutations

def primeNumber3(n):
    num = set(range(2,n+1))     # {2, 3, ..., n} (set)
    for i in range(2,n+1):
        if i in num:            # 만약 i가 num 집합에 있다면
            num -= set(range(2*i, n+1, i))  # i배수는 num 집합에서 제외
    return len(num)


def solution(nums):
    # permutations(list, 갯수)
    new_list = list(permutations(nums, 3))
    sum_list = set([sum(i) for i in new_list])
    prime_list = []
    for i in sum_list:
        prime_list.append(primeNumber3(i))

    print(sum_list)
    print(prime_list)

    return answer
'''



from itertools import combinations          # 중복허용(X), 순서의미(O) 인 조합을 import

"""소수 판별 함수"""
def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):      # math를 사용하지 않고 (num//2)+1 까지로 설정
            if num%n == 0:
                return False
        
        return True

def solution(nums):
    answer = 0
    cmb = list(combinations(nums,3))        # nums배열을 3개씩 조합 후 list로 변경
    for arr in cmb:
        if is_prime_number(sum(arr)):       # cmb를 하나씩 가져와 sum한 값을 소수 판별 함수로 넘겨줌
            answer += 1                     # return 값이 True이면 count(=answer) +1
    
    return answer


print(solution([1,2,3,4]))