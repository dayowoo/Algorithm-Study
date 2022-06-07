'''
1. 더할 수 있는 모든 경우의 수 (이중 for문으로)
2. x[0]+y[0],y[1]...
3. 리스트에서 중복 제거 오름차순 정렬
'''

'''
for i in list:
    print(i)

for i in range(0, len(numbers)):
    print(numbers[i])
'''

'''
- list.sort() :
- sorted(list) : 새로운 정렬된 리스트를 반환, 어떤 객체든 가능, 일반적으로 더 편함
'''

def solution(numbers):
    sum = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i==j:
                pass
            else:
                sum.append(numbers[i]+numbers[j])
    return sorted(set(sum))


print(solution([2,1,3,4,1]))



# 다른 풀이
def solution2(numbers):
    answer = []
    for i in range(len(numbers)):
        # i+1이 key
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))