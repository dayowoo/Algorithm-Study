# 1
print('Hello')


# 2
print("Hello World")


# 3
print("Hello")
print("World")

'''
print("Hello\nWorld")
'''


# 4
print("'Hello'")


# 5
print("\"Hello World\"")

'''
print('"Hello World"')
'''


# 6 
print("\"!@#$%^&*()'")

'''
print('"!@#$%^&*()\'')
'''


# 7
# 다음 경로를 출력하시오.
# "C:\Download\'hello'.py"
print("\"C:\\Download\\'hello'.py\"")


# 8
# print("Hello\nWorld")를 출력하시오.
print('print("Hello\\nWorld")')


# 10
n = input()
n = int(n)
print(n)


# 11
f = input()
f = float(f)
print(f)


# 12
a = input()
b = input()
print(a)
print(b)


# 13
a = input()
b = input()

print(b)
print(a)


# 14
a = input()
f = float(a)

print(f)
print(f)
print(f)


# 15
# 공백을 두고 입력된 정수 2개를 입력받아 줄바꿔 출력 (split())
a, b = input().split()
print(a)
print(b)


# 16
a,b = input().split()
print(b,a)


# 17
s = input()
print(s, s, s)


# 18
# input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.
a, b = input().split(':')
print(a, b, sep=':')


# 19
# print(date, type(date)) // ['2020','01','01'] <class 'list'>
date = input().split('.')
date.reverse()
print('-'.join(date))


# 20
info = input()
infoo= info.replace('-','')
print(infoo)