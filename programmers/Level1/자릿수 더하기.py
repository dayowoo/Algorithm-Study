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



# 다른사람 풀이
def sum_digit2(number):
    if number < 10:
        return number
    return (number%10) + sum_digit(number//10)

print(sum_digit2(123))