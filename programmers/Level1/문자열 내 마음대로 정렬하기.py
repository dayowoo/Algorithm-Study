'''
- n을 문자열 앞에 붙여 큰 순서대로 정의한다.
'''

def strange_sort1(strings, n):
    answer = []
    for i in strings:
        answer.append(i[n]+i)
    answer.sort()
    return [i[1:] for i in answer]

print(strange_sort1(["sun", "bed", "car"], 1))


# 다른사람 풀이

# 람다 함수 활용
def strange_sort2(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])


# sort함수를 만들어 key로 사용
def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings