'''
<약수 알고리즘>
def divisor(number):
    index = 1   
    count = 0   # 약수의 개수
    while index <= number:
        if number % index ==0:
            count += 1
        index += 1
'''

def divisor(number):
    index = 1   
    count = 0   # 약수의 개수
    while index <= number:
        if number % index ==0:
            count += 1
        index += 1
    return count


def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


print(solution(13,17))