'''
1. 중첩 리스트 만들기 [4,'true'] 이렇게..
2. flase가 있으면 -붙이기
3. 합산
'''

'''
# zip : 
for l,w in zip(length,weight):
  fish_data.append([l,w])

# 리스트 내포(comprehension)
fish_data = [[l,w] for l,w in zip(length,weight)]
fish_data

'''

# 이렇게 하면 1,0이 들어 있을때 무조건 True, False이기 때문에 문제가 됨..
def solution1(absolutes, signs):
    new_list = []
    for i,j in zip(absolutes, signs):
        new_list.append([i,j])

    new_list2 = []
    for i in new_list:
        if True in i:
            new_list2.append(i[0])
        elif False in i:
            new_list2.append(-i[0])

    return sum(new_list2)


def solution(absolutes, signs):
    new_list = []
    for i in range(len(absolutes)):
        if signs[i] == False:
            new_list.append(-absolutes[i])
        elif signs[i] == True:
            new_list.append(absolutes[i])

    return sum(new_list)

print(solution([1,2,3], [False, False, True]))



# 다른 풀이
def solution2(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
