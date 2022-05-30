'''
- str.count('') : 문자열에서 해당 문자가 몇번 존재하는지 카운트, 존재X -> 0반환
'''

def numPY(s):
    p_count = s.count('p')+s.count('P')
    y_count = s.count('y')+s.count('Y')
    if p_count == y_count:
        return True
    else:
        return False


print(numPY("pPoooyY"))


# 다른 사람 풀이
# 모두 lower로 바꿔서 count, if-else없이 한줄로 알아서 True, False 반환
def numPY2(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')