'''
- sorted(list, reverse=True) : 리스트 뒤집기
'''

def solution(s):
    s_list = sorted(list(s), reverse=True)
    return ''.join(s_list)
    


print(solution("Zbcdefg"))