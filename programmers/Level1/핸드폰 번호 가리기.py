'''
1. 뒤에서부터 슬라이싱 
2. 문자열 바꾸기

def solution(phone_number):
    answer = phone_number.replace(phone_number[-4:],'****')
    return answer
'''

def hide_numbers(phone_number):
    star = '*'*len(phone_number[0:-4])
    answer = phone_number.replace(phone_number[0:-4],star)
    return answer


# 다른 풀이
def hide_numbers2(s):
    print(s[-4:], s[:-4])
    return '*' * (len(s) - 4) + s[-4:]


print(hide_numbers2('01033334444'))