'''
< 탐욕법 / 그리디 문제>
- 양 옆 학생에게 빌려줄 수 있으면, 왼쪽 요소부터 탐색해야 함

- set : 집합 연산을 지원함, -연산을 통해 차집합을 구할 수 있음.

'''

def solution(n, lost, reserve):
    # 빌려줄 수 있는 사람: reserve - lost
    set_reserve = set(reserve)-set(lost)
    # 체육복 꼭 빌려야 하는 사람: lost - reserve
    set_lost = set(lost)-set(reserve)

    '''
    1. set_reserve loop
    2. 왼쪽(i-1)이 체육복이 없다면 먼저 빌려주기
    3. 오른쪽(i+1)이 체육복이 없다면 빌려주기
    '''
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    # 전체 학생 - 남은 잃어버린 학생 수
    return n-len(set_lost)


print(solution(5, [2,4], [1,3,5]))