'''
1. len(s) % 2 == 0:

'''


def string_middle(s):
    # if len(s%2): (1->True, 0->False)
    if len(s)%2 == 1:
        n = len(s)//2
        return s[n]
    else:
        n = len(s)//2-1
        return s[n:n+2]


print(string_middle("abcd"))



# 다른사람 풀이
def string_middle2(str):
    '''
    
    '''
    return str[(len(str)-1)//2:len(str)//2+1]
