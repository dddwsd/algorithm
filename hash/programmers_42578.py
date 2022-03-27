# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict
from itertools import combinations
def solution(clothes):
    answer = 0
    dic = defaultdict(int)
    for _, type in clothes:
        dic[type] += 1
    
    keys = list(dic.values())
    for length in range(len(dic)):
        length += 1
        for item in list(combinations(keys,length)):


    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
result = 5
if solution(clothes) == result:
    print('Success')
else:
    print('Fail')

clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
result = 3
if solution(clothes) == result:
    print('Success')
else:
    print('Fail')