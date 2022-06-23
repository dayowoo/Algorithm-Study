'''
1. 공백 기준으로 리스트 저장
2. i[0].upper() -> 대문자 변환
3. 
'''

'''
def solution(s):
    answer = list(map(str, s.split()))
    new_list = []
    new = []
    for i in answer:
        new_list.append(i.replace(i[0], i[0].upper()))
    for i in new_list:
        new.append(i.replace(i[1:], i[1:].lower()))
    result = ' '.join(s for s in new)
    return result
'''

def solution(s):
    answer=''
    s=s.split(' ')
    for i in range(len(s)):
        if not s[i][0].isdecimal():
            s[i]=s[i][0].upper()+s[i][1:].lower()
    answer=' '.join(s)
    return answer

print(solution("for the last week"))