def water_melon(n):
    answer = ('수박'*n)
    return answer[:n]

print(water_melon(3))


def water_melon2(n):
    answer = ''
    
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    
    return answer