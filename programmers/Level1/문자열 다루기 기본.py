'''
1. 문자열 길이가 4,6인지 확인
2. 숫자로만 구성되어 있는지 확인 : isdigit
'''

def alpha_string46(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False

print(alpha_string46("a1234"))


# 다른 사람 풀이
def alpha_string462(s):
    return s.isdigit() and len(s) in (4, 6)