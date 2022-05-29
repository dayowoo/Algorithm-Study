'''
- chr: 정수를 인자로 받고, 정수에 해당하는 유니코드 문자를 반환함. 97 -> 'a'
- ord: 문자를 인자로 받고, 문자에 해당하는 유니코드 정수를 반환. 'a' -> 97
- list(str), str.split()
- ''.join(list) : 리스트 문자열 합치기
'''

# 테스트케이스 1번말고 나머지는 어떻게 푸는지 모르겠음..
def caesar(s, n):
    answer = list(s)
    ord_list = []
    chr_list = []
    for i in range(len(answer)):
        ord_list.append(ord(answer[i])+n)
        chr_list.append(chr(ord_list[i]))
    return ''.join(chr_list)

print(caesar("AB",1))



### 다른사람 풀이

def caesar2(s,n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
 
    return "".join(s)