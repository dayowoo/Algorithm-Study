
# x의 값을 1씩 증가시키면서 찾음
def solution(n):
    x = 1
    while True:
        if n%x ==1:
            # return x
            x= x
            break
        else:
            x+=1
    return x


print(solution(10))


# 다른 사람 풀이
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]