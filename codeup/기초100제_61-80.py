# 61
a, b = input().split()
result = int(int(a)|int(b))
print(result)


# 62
'''
비트단위(bitwise) 연산자,
~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
<<(bitwise left shift), >>(bitwise right shift)
'''
a, b = map(int,input().split())
result = a^b        # xor 연산
print(result)
'''
a, b = map(int, input().split())
print(a if a > b else b)
'''


# 63
a, b = map(int, input().split())
c = (a if (a>=b) else b)
print(c)


# 64
a, b, c = map(int, input().split())
d = (a if a<b else b) if ((a if a<b else b)<c) else c
print(d)


# 65
a, b, c = map(int, input().split())
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)


# 66
data = map(int, input().split())

for i in data:
    if i%2==0:
        print("even")
    else:
        print("odd")


# 67
a = int(input())
if (a<0 and a%2==0):
    print('A')
elif (a<0 and a%2==1):
    print('B')
elif (a>0 and a%2==0):
    print('C')
elif (a>0 and a%2==1):
    print('D')


# 68
n = int(input())
if n>=90 :
    print('A')
elif n>=70 :
    print('B')
elif n>=40 :
    print('C')
else :
    print('D') 


# 69
a = input()
if a=='A':
    print('best!!!')
elif a=='B':
    print('good!!')
elif a=='C':
    print('run!')
elif a=='D':
    print('slowly~')
else:
    print('what?')


# 70
a = int(input())
winter = [12,1,2]
spring = [3,4,5]
summer = [6,7,8]
fall = [9,10,11]
if a in winter:
    print("winter")
if a in spring:
    print("spring")
if a in summer:
    print("summer")
if a in fall:
    print("fall")

'''
season = ''
if(month in [12, 1, 2]):
    season = 'winter'
elif(month in [3, 4, 5]):
    season = 'spring'
elif(month in [6, 7, 8]):
    season = 'summer'
else:
    season = 'fall'
print(season)
'''


# 71
n = 1      #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
while n!=0 :
  n = int(input())
  if n!=0 :
    print(n)
'''
i = True
while(i):
    num = int(input())
    if(num == 0):
        i = False
    else:
        print(num)
'''


# 72
n = int(input()) 
while n>0:
    print(n)
    n-=1


# 73
num = int(input())
while(num > 0):
    num -= 1
    print(num)


# 74
c = ord(input())            # ord: 알파벳의 정수값
t = ord('a')               
while t<=c :
  print(chr(t), end=' ')    # 끝에 공백출력, \n: 줄바꿈
  t += 1


# 75
a = int(input())
for i in range(0,a+1):
    print(i)


# 76
a = int(input())
for i in range(a+1):
    print(i)


# 77
n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==0 :
    s += i
print(s)


# 78
a=1
while a==1:
    n = input()
    print(n)
    if n=='q':
        a=0
'''
c = ''
while(c != 'q'):
    c = input()
    print(c)
'''


# 79
a = int(input())
i=0
s=0
while s<a:
    i+=1 
    s+=i
print(i)


# 80
n, m = map(int, input().split())
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i, j)