'''
1. 1~n까지 for문 돌리기
2. i번째 수가 소수인지 판별
3. % != 0 : pass, 아니면 append

<약수 원리 활용>
- n의 루트값으로 떨어지는지 확인한다
ex. 25%5=0 -> False

<에라스토네스의 체>


'''
import math


# 시간초과

def primeNumber(n):
    answer = []
    for n in range(2,n+1):
        for i in range(2,n):
            if n%i == 0:
                break
        else:
            answer.append(n)
    print(answer)
    return len(answer)


def primeNumber2(n):
    count = 0
    for n in range(2, n+1):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            count+=1
    return count




# 다른 풀이
def primeNumber3(n):
    num = set(range(2,n+1))     # {2, 3, ..., n} (set)
    for i in range(2,n+1):
        if i in num:            # 만약 i가 num 집합에 있다면
            num -= set(range(2*i, n+1, i))  # i배수는 num 집합에서 제외
    return len(num)

print(primeNumber3(10))