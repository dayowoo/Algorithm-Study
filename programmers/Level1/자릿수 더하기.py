'''
1. 입력된 글자의 자릿수를 센다.
2. a[i] + ... 
'''

def sum_digit(n):
    a = len(str(n))
    b = str(n)
    c = []
    for i in range(0, a):
        c.append(int(b[i]))
    answer = sum(c)
    return answer

print(sum_digit(1))



# 다른사람 풀이 - 재귀구조: a함수 내에서 a함수 호출
def sum_digit2(number):
    # 한자리수의 경우 그냥 출력
    if number < 10:
        return number
    # 나머지 + 몫
    return (number%10) + sum_digit(number//10)

print(sum_digit2(123))


def sum_digit3(number):
    return sum(map(int,str(number)))


def sum_digit4(number):
    return sum([int(i) for i in str(number)])