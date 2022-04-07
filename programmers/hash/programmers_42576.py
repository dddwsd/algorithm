# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import defaultdict
def solution(participant, completion):
    part_dic = defaultdict(int)
    for part in participant:
        part_dic[part] += 1
    
    for com in completion:
        part_dic[com] -= 1
        if part_dic[com] == 0:
            del part_dic[com]
    return list(part_dic.keys())[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
result = 'leo'
if solution(participant, completion) == result:
    print('Success')
else:
    print('Fail')

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
result = 'vinko'
if solution(participant, completion) == result:
    print('Success')
else:
    print('Fail')

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
result = 'mislav'
if solution(participant, completion) == result:
    print('Success')
else:
    print('Fail')