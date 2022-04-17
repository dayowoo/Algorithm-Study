h, w= map(int, input().split())
n = int(input())

location = [[0] * w for _ in range(h)]
'''
location = []
for i in range(h):
    location.append([])
    for j in range(w):
        location[i].append(0)
'''

# 채우기
for i in range(n):
    l,d,x,y = map(int, input().split())
    
    for j in range(l):
        if d==1:
            location[x-1][y-1+j]=1
        else:
            location[x-1+j][y-1]=1

# 출력
for i in range(h):
    for j in range(w):
        print(location[i][j], end=" ")
    print(end='\n')
