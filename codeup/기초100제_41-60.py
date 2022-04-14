# 41
a, b = input().split()
result = int(a)%int(b)
print(result)


# 42
a=float(input())
print( format(a, ".2f") )


# 43
f1, f2= input().split()
result = float(f1)/float(f2)
print(format(result,".3f"))


# 44
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)     # 몫
print(a%b)      # 나머지
print(format(a/b,".2f"))



# 45
a, b, c = input().split()
sum = int(a)+int(b)+int(c)
avg = format(sum/3,".2f")
print(sum, avg)



# 46
a = int(input())
print(a<<1)


# 47
a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)


# 48
a, b = input().split()
a = int(a)
b = int(b)

print(a<b)


# 49
a, b = input().split()
a = int(a)
b = int(b)
print(a==b)


# 50
a, b = input().split()
a = int(a)
b = int(b)
print(b>=a)


# 51
a, b = input().split()
a = int(a)
b = int(b)
print(a!=b)


# 52
n = int(input())
print(bool(n))      # 0이면 False, 0이 아닌 정수면 True


# 53
a = bool(int(input()))
print(not a)


# 54
a, b = input().split()
print(bool(int(a)) and bool(int(b)))


# 55
a, b = input().split()
print(bool(int(a)) or bool(int(b)))


# 66
a, b, c = input().split()

if int(a)%2 ==0:
    print("even")
else:
    print("odd")
if int(b)%2==0:
    print("even")
else:
    print("odd")
if int(c)%2==0:
    print("even")
else:
    print("odd")



# 56
a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print(a!=b)         # print((a and (not b)) or ((not a) and b))


# 57
a, b = map(int, input().split())
print(bool(a)==bool(b))


# 58
# is False, is True
a, b = map(int, input().split())
print(bool(a) is False and bool(b) is False)


# 59
# 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)
# ~ : 비트별로 반대로 변환 후 계산 1->0, 0->1
a = int(input())
print(~a)


# 60 ( & : 비트단위연산자)
a, b = map(int, input().split())
print(a & b)