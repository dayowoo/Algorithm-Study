'''
1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. -> 반복한 횟수?
'''


from itertools import count


def collatz(num):
    count = 0
    while num>=1:
        if count>=500:
            return -1
        if num==1:
            return count
        if num%2==0:
            num = num/2
            count +=1
        else:
            num = (num*3)+1
            count +=1

# 다른 사람 풀이
def collatz2(num):
    for i in range(500):
        if num==1:
            return i
        if num%2==0:
            num = num/2
        else:
            num = (num*3)+1
    return -1


print(collatz2(626331))