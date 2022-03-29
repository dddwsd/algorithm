# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    only_lost = list(set(lost) - set(reserve))
    only_reserve = list(set(reserve) - set(lost))
    for item in sorted(only_reserve):
        if item-1 in only_lost and item-1 > 0:
            only_lost.remove(item-1)
        elif item+1 in only_lost and item+1 <= n:
            only_lost.remove(item+1)
    answer = n - len(only_lost)
    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
result = 5
if solution(n, lost, reserve) == result:
    print('Success')
else:
    print('Fail')

n = 5
lost = [2, 4]
reserve = [3]
result = 4
if solution(n, lost, reserve) == result:
    print('Success')
else:
    print('Fail')

n = 3
lost = [3]
reserve = [1]
result = 2
if solution(n, lost, reserve) == result:
    print('Success')
else:
    print('Fail')

n = 5
lost = [1, 2, 3, 4]
reserve = [1]
result = 2
if solution(n, lost, reserve) == result:
    print('Success')
else:
    print('Fail')