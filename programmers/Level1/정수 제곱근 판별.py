'''
1. 루트 구하기
x^2 = n, x = math.sqrt(n)
x**0.5

2. 의미없는 소숫점(.0) 생략
"%g"%(5.0)

3. 양수(정수)인지 실수인지 판별 : str.isdigit()
오직 0을 포함한 양수형 정수로만 이루어진 문자열만 True
"-2".isdigit(), "1.234".isdigit() 둘다 False

'''

import math

# 테스트 2, 4는 통과 못함
def nextSquare(n):
    x = str("%g"%(n**0.5))
    if x.isdigit() is True:
        x = int(x)
        return (x+1)**2
    else:
        return -1



# 다른 풀이
'''
x%1 == 0 : 양의정수 판별
'''
def nextSquare2(n):
    x = math.sqrt(n)
    if x % 1 == 0:  # 나머지가 0 -> 양의정수
        answer = (x+1)**2
    else:
        answer = -1
    return answer

print(nextSquare2(121))
