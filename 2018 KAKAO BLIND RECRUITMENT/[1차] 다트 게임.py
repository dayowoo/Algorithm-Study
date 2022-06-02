'''
1. 라운드 분리하기
2. 
'''

# 전체 탐색

'''
def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:
        print(i)
        if i.isnumeric():
            print(i, type(i))
            n += i
        elif i == 'S':
            n = int(n)**1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            score.append(n)
            n = ''
        elif i == '*':
            if 
    print(n, score)
    return 0


print(solution("1S2D*3T"))
'''