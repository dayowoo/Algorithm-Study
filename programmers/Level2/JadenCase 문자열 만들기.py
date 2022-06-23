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


def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer


# 다른 풀이
'''
- title: 문자열을 단어 앞만 대문자로 바꿀 수 있음
'''
def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()

print(Jaden_Case("3people unFollowed me for the last week"))