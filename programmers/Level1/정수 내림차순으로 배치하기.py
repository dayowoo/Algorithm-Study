'''
1. 정수 > 문자열 > 리스트 변환
- nList = list(str(n))
- list(map(int, str(n)))

2. 리스트내에서 내림차순 정렬
- list.sort(reverse=True)

3. 리스트 > 정수 변환
- "".join(list)) 함수 알아두기
'''

def solution(n):
    nList = list(str(n))
    nList.sort(reverse=True)
    return "".join(nList)

print(solution(118372))