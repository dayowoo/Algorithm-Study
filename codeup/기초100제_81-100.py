# 81
n = input()
for i in range(1, 15 + 1):
    print('%X*%X=%X' %(int(n, 16), int(hex(i), 16), (int(n, 16) * int(hex(i), 16))))


# 82
n = int(input())
for i in range(1,n+1):
    if (i%10==3 or i % 10 == 6 or i % 10 == 9):
        print('X', end=' ')
    else:
        print(i, end=' ')


# 83
r, g, b = map(int, input().split())
for i in range(0,r):
    for j in range(0,g):
        for q in range(0,b):
            print('{} {} {}'.format(i, j, q))
print(r*g*b)


# 84
# 8 = 2**3 = pow(2,3)
h, b, c, s = map(int, input().split())
data = round((((h * b * c * s /8)/1024)/1024),1)
print(f'{data} MB')


# 85
w, h, b = map(int, input().split())
# data = round(((((w*h*b)/8)/1024)/1024),2)
data = round(((w*h*b)/2**300),2)
print(f'{data} MB')     # print('{:.2f} MB'.format(mb))


# 86
n = int(input())
sum = 0
a = 0
while True:
    sum += a
    a += 1 
    if sum >= n:
        break
print(sum)


# 87
n = int(input())
for i in range(0, n+1):
    if i%3==0:
        pass
    else:
        print(i)


# 88 등차수열
a, d, n = map(int, input().split())
print(a+((n-1)*d))


# 89 등비수열
a, r, n = map(int, input().split())
print(a*(r**(n-1)))
'''
total = a
for i in range(a, a + n - 1):
	total *= b
'''


# 90 수열
a, m, d, n = map(int, input().split())
total = a
for i in range(a, a+n-1):
	total = total * m + d 
print(total)


# 91 최소공배수
a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)


# 92 문제이해를 못하겠음
from random import randint

n = int(input())
temp = [0] * 23
nums = input().split()
for i in nums:
    temp[int(i)-1] += 1
for i in temp:
    print(i, end=' ')


# 93 문제이해를 못하겠음
n = int(input())
nums = input().split()
nums.reverse()
for i in nums:
    print(int(i), end=' ')


# 94
n = int(input())
nums = map(int, input().split())
print(min(nums))


# 95 2차원 리스트
# 빈 리스트 생성
d=[]
for i in range(20) : 
  d.append([])
  for j in range(20) :  
    d[i].append(0)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20): 
        print(d[i][j], end=" ")
    print()     # 줄바꿈


# 96
location = []
for i in range(19):
    location.append([])
    for j in range(19):
        location[i].append(0)
    
for i in range(19):
    location[i] = list(map(int, input().split()))

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if location[x-1][j] == 0:
            location[x-1][j] = 1
        else: 
            location[x-1][j] = 0
            
        if location[j][y-1] == 0:
            location[j][y-1] = 1
        else:
            location[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(location[i][j], end=" ")
    print()


# 6097