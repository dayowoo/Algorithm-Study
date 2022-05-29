'''
- if type(x) is int/str/list

'''


def strToInt(s):
    if type(s) is int:
        return str(s)
    elif type(s) is str:
        return int(s)


print(strToInt(+1))