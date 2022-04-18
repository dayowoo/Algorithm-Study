'''
for문을 리스트에 내포
[ 표현식 for 항목 in 리스트 or 튜플 if 조건문 ] # if는 생략 가능
ex. [num * 3 for num in list]
ex. [ num * num2 for num in list for num2 in list]

'''

def sumMatrix(arr1, arr2):
    answer = [[arr1[i][j]+arr2[i][j] for j in range(len(arr1[0]))]for i in range(len(arr1))]
    return answer


def sumMatrix2(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


def sumMatrinx3(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer



print(sumMatrinx3([[1,2],[2,3]],[[3,4],[5,6]]))