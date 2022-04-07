# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict
def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for _, type in clothes:
        dic[type] += 1
    
    for val in list(dic.values()):
        answer *= (val+1)
    return answer-1

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