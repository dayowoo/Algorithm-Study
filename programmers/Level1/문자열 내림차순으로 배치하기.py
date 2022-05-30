'''
- sorted(list, reverse=True) : 리스트 뒤집기

s = 'abcde'
s_list = list(s)  # reverse 함수를 사용하기 위해 문자열을 list로 치환
s_list.reverse()  # reverse 함수를 사용해 문자열 리스트를 거꾸로 뒤집음

print(''.join(s_list))  # 거꾸로 뒤집어진 리스트를 연결해서 출력


or 

s = 'abcde'
print(''.join(reversed(s)))  # 'edcba'


s = 'abcde'
print(s[::-1])  # 'edcba'

'''

def solution(s):
    s_list = sorted(list(s), reverse=True)
    return ''.join(s_list)
    


print(solution("Zbcdefg"))