

def solution(price, money, count):
    price_list = []
    for i in range(1, count+1):
        price_list.append(price*i)
    sum_list = sum(price_list)
    if sum_list>=money:
        return sum_list-money
    else:
        return 0


print(solution(3,20,4))


# 다른 사람 풀이
# 리스트 요소를 곱해서 total에 넣기
def solution(price, money, count):
    total = sum(range(1,count+1)) * price
    answer = total - money if total != money else 0

    return answer