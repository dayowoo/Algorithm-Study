'''
1. 입력된 수의 자릿수의 합을 구한다.
2. if x%sum == 0: True, else: False
'''

def Harshad(x):
    num = str(x)
    sum = 0
    # 입력된 자릿수의 합 구하기
    for i in range(len(num)):
        sum += int(num[i])
    # return n % sum(nums) == 0
    if x % sum == 0:
        answer = True       # return True
    else:
        answer = False
    return answer


# 다른 풀이
def Harshad2(n):
    # 리스트로 만들어서 리스트 내의 합을 구한다
    return n % sum([int(c) for c in str(n)]) == 0


print(Harshad2(10))