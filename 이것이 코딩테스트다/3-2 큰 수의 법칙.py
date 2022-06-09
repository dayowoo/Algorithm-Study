'''
n: 배열의 크기, m: 숫자 더하는 총 횟수, k: 연속으로 더할 수 있는 횟수
입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 됨.
연속으로 더할 수 있는 횟수는 최대 K번이므로 ‘가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산’을 반복하면 됨.

- map(int, input().split())
- list(map(int, input().split())
'''

def solution(n, m, k, data):
    data.sort()     # 리스트 큰 수 정렬
    first = data[n-1]    # 가장 큰 수, 0부터 시작해서 -1 해줘야 됨.
    second = data[n-2]
    
    result = 0
    while True:
        for i in range(k):  # 가장 큰 수를 k번 더하기
            if m==0:
                break
            result += first
            m -= 1
        if m==0:
            break
        result += second
        m -= 1

    return result

'''
- key: 반복되는 수열에 대해 파악하기
- 수열이 반복되는 횟수: M/(K+1)   # K+1: 큰 수 최대 더한 횟수 + 작은 수 한번
- 가장 큰 수가 등장하는 횟수: (M/(K+1))*K
'''
# 시간 초과 통과 버전
def solution2(n, m, k, data):
    data.sort()
    first = data[n-1]
    second = data[n-2]

    # 가장 큰 수가 등장하는 횟수
    count = int(m/(k+1))*k
    count += m%(k+1)

    result = 0
    result += count*first
    result += (m-count)*second      # 총 더한 수- 큰 수가 더해지는 횟수
    return result




n, m, k = map(int, input().split())
data = list(map(int, input().split()))
print(solution2(n,m,k,data))



