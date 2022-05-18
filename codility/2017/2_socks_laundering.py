# https://app.codility.com/programmers/trainings/3/socks_laundering/start/

from collections import defaultdict

def solution(K, C, D):
    # write your code in Python 3.6
    answer = 0 
    clean_count = defaultdict(int)
    for clean in C:
        clean_count[clean] += 1
        if clean_count[clean] == 2:
            answer += 1
            clean_count[clean] = 0

    dirty_count = defaultdict(int)
    for dirty in D:
        if K == 0:
            break
        if clean_count[dirty] == 1:
            answer += 1
            K -= 1
            clean_count[dirty] = 0
        else:
            dirty_count[dirty] += 1

    if K > 0 :
        dirty_socks = sorted(dirty_count.values(), reverse=True)
        for item in dirty_socks:
            num = min(K // 2, item // 2)
            answer += num
            K -= num * 2
            if K < 2:
                break

    return answer


K = 6
C = [1, 2]
D = [1, 3, 3, 3, 2, 5, 5]
result = 4
if solution(K, C, D) == result:
    print('Success')
else:
    print('Fail')