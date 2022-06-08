'''
1. 10진법 > 3진법
2. 3진법 뒤집기 : str[::-1] / reversed(str)
3. 3진법 > 10진법 : int(string, base)

- 10진수 > 2,8,6진수: bin(), oct(), hex()
- 진법표시 지우기 : bin()[2:]
'''

def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    num = rev_base[::-1]
    return int(num[::-1],3)

print(solution(45))


# 다른 풀이

def solution2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer