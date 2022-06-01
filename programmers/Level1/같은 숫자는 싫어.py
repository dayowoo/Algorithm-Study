'''
# 리스트 중복 요소 제거하기

* 순서 상관 X *
my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
my_set = set(my_list) #집합set으로 변환
my_list = list(my_set) #list로 변환
print(new_list)

* 순서 상관 o *
my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
new_list = []
for v in my_list:
    if v not in new_list:
        new_list.append(v)
print(new_list)


'''


# 테스트케이스 17 통과 안됨
def solution(arr):
    answer = []
    for i in range(0,len(arr)):
        if len(arr)==1:
            answer=arr
        if i+1 < len(arr):
            if arr[i] != arr[i+1]:
                answer.append(arr[i])
    if answer[-1] != arr[-1]:
        answer.append(arr[-1])
    return answer


print(solution([0]))


def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a



def no_continuous2(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
