'''
윤년 : 4년에 한번씩 2/29일이 생기는 날 (366일)
2016.1.1 : 금요일

// : 몫
% : 나머지
'''

import datetime

# def getDayName(a,b):
#     t = 'MON TUE WED THU FRI SAT SUN'.split()
#     return t[datetime.datetime(2016, a, b).weekday()]




# 다른 사람 풀이
def getDayName(a,b):
    # 12달의 끝 숫자를 입력해줌
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    '''
    sum(months[:4]) = 31+29+31+30 = 121
    b-1 = 23
    (121+23)%7 = 4
    days[4] = "TUE"
    '''
    print((sum(months[:a-1])+b-1)%7)
    return days[(sum(months[:a-1])+b-1)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))