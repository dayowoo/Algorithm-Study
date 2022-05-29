'''
1. 공백을 기준으로 slice후 리스트 저장: str.slice()
2. list[i] %2 == 0 : upper
3. list[i] %2 != 0 : lower
'''

def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j%2==0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]
    
    

print(solution("try hello world"))