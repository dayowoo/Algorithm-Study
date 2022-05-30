'''
'''

def adder(a, b):
    answer = []
    if a>b:
        for i in range(b, a+1):
            answer.append(i)
        return sum(answer)
    elif b>a:
        print(a,b)
        for i in range(a, b+1):
            answer.append(i)
        return sum(answer)
    elif a==b:
        return a

print(adder(3,5))



# 다른 사람 풀이
def adder2(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))
