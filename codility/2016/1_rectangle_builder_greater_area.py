# https://app.codility.com/programmers/trainings/2/rectangle_builder_greater_area/start/

# 69% score - O(n^2)
from collections import defaultdict
from itertools import combinations

def solution(A, X):
    # write your code in Python 3.6
    answer = 0
    length_dic = defaultdict(int)
    combi_list = []
    for fence in A:
        length_dic[fence] += 1
        if length_dic[fence] == 2:
            combi_list.append(fence)
        elif length_dic[fence] == 4:
            if fence ** 2 >= X:
                answer += 1

    for items in list(combinations(combi_list, 2)):
        w, h = items
        if w*h >= X:
            answer += 1
    return answer

# 69% score
from collections import defaultdict

def solution(A, X):
    # write your code in Python 3.6
    answer = 0
    A = sorted(A)
    fence_count = defaultdict(int)
    rec_dic = {}

    for fence in A:
        fence_count[fence] += 1
        if fence_count[fence] == 2:
            for side in rec_dic:
                if side * fence >= X:
                    rec_dic[side].append(fence)
            rec_dic[fence] = []
        if fence_count[fence] == 4:
            if fence ** 2 >= X:
                rec_dic[fence].append(fence)
    
    for values in rec_dic.values():
        answer += len(values)
    return answer

# 100% - binary search
from collections import defaultdict

def solution(A, X):
    # write your code in Python 3.6
    answer = 0
    length_dic = defaultdict(int)
    fences = []
    for fence in sorted(A):
        length_dic[fence] += 1
        if length_dic[fence] == 2:
            fences.append(fence)
        elif length_dic[fence] == 4:
            if fence ** 2 >= X:
                answer += 1

    fences_size = len(fences)
    for idx in range(fences_size):
        start = idx + 1
        end = fences_size - 1
        while start <= end:
            mid = (start + end) // 2
            if fences[idx] * fences[mid] >= X:
                end = mid - 1
            else:
                start = mid + 1
        #answer += fences_size - (end + 1)
        answer += fences_size - start
        if answer > 1000000000:
            return -1
    return answer



if solution([1, 2, 5, 1, 1, 2, 3, 5, 1], 5) == 2:
    print('Success')
else:
    print('Fail')