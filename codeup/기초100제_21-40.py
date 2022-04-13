# 21
s = input()
for i in range(0,6):
    print(s[i])


# 22
s = input()
print(s[0:2],s[2:4],s[4:6])


# 23
time = input().split(':')
print(time[1])


# 24
w1, w2 = input().split()
s = w1 + w2
print(s)


# 25
a, b = input().split()
c = int(a) + int(b)
print(c)


# 26
f1 = float(input())
f2 = float(input())
print(f1+f2)


# 27
a = input()
n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력


# 28
'''
n = int(input())
print('%x'.upper()%n)
'''
a = input()
n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%X'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 대문자 형태 문자열로 출력


# 29
a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력


# 30
n = ord(input())
print(n)


# 31
c = int(input())
print(chr(c))


# 32
n = int(input())
print(-n)


# 33
n = ord(input())
print(chr(n+1))


# 34
a,b = input().split()
c = int(a) - int(b)
print(c)


# 35
f1, f2 = input().split()
m = float(f1) * float(f2)
print(m)


# 36
w, n = input().split()
print(w*int(n))


# 37
n = input()
s = input()
print(int(n)*s)


# 38
a, b = input().split()
c = int(a)**int(b) 
print(c)


# 39
f1, f2 = input().split()
f3 = float(f1)**float(f2)
print(f3)


# 40
a,b = input().split()
print(int(a)//int(b))