'''
1. if h>w , h,w = w,h
2. max(w) * max(h)
'''

def solution(sizes):
    for i in sizes:
        if i[1]>i[0]:
            i[1],i[0] = i[0],i[1]
    w = max([i[0] for i in sizes])
    h = max([i[1] for i in sizes])
    return w*h


print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))


# 다른 사람 풀이
def solution(sizes):
    '''
    max(max(x) for x in sizes) : 19 // 큰 쌍중에 가장 큰 수
    max(min(x) for x in sizes) : 7 // 작은 쌍중에 가장 큰 수
    '''
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)