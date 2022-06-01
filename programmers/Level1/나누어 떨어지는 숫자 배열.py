'''
- del arr[i] : i번째 인덱스 삭제
- arr.remove[i] : 배열에서 i를 삭제
- return arr.sort()는 None 을 반환함 -> return 전 sort 해주기
- sort(reverse=True) : 오름차순, sort(reverse=False) : 내림차순
- a_sub_b = [x for x in a if x not in b]
'''

# 문제점 : 삭제된 후에 인덱스에 변화가 생김
def solution(arr, divisor):
    for i in arr:
        if i%divisor != 0:
            arr.remove(i)
    arr.sort()
    return arr



def solution2(arr, divisor):
    new_list=[]
    for i in arr:
        if i%divisor != 0:
            new_list.append(i)
    if arr == new_list:
        return -1
    sub_list = [x for x in arr if x not in new_list]
    sub_list.sort()
    return sub_list



def solution3(arr, divisor):
    new_list=[]
    for i in arr:
        if i%divisor == 0:
            new_list.append(i)
    #  if not new_list
    if len(new_list) == 0:
        return -1
    new_list.sort()
    return new_list

######################## 테스트케이서 6,7,8 통과 못함 왜징


def solution4(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]



print(solution3([3,2,6], 10))