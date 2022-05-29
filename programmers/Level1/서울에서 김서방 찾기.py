
def solution(seoul):
    # return ('김서방은 %d에 있다' %seoul.index('Kim'))
    answer = "김서방은 {n}에 있다".format(n=seoul.index("Kim"))
    return answer


print(solution(["Jane", "Kim"]))