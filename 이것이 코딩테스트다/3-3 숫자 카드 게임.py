'''
각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾기.
'''

def solution(data):
    result = 0
    print(data)
    for i in range(len(data)):
        min_value = min(data[i])
        result = max(result, min_value)
    return result

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

print(solution(data))