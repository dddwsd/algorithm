# https://programmers.co.kr/learn/courses/30/lessons/43164

"""
"ICN" : "AAA", "BBB"
"BBB" : "ICN"
"AAA" : "DDD", "CCC"
"DDD" : "AAA"
"""


from collections import defaultdict
def solution(tickets):
    visit = defaultdict(lambda : defaultdict(int))
    tickets.sort(key=lambda x:x[1])
    for ticket in tickets:
        start, end = ticket
        visit[start][end] += 1

    # DFS
    # 도착지들을 하나씩 꺼내서 가봄
    # 계속 가다가 마지막에 더이상 갈곳이 없다.
    #     이때 route에 value가 남이 있지 않으면 True return
    #     이때 route에 value가 남이 있지 있으면 False return
    #         갈림길로 돌아와 다음 목적지 가봄
    #         갈림길에서 모든 목적지 돌았는데도 성공 못하면 길들 다시 넣고 이전 갈림길로 돌아감  
    length = len(tickets)
    def found(begin, visit, answer):
        if len(answer) == length + 1:
            return True, answer
        if begin not in visit:
            if len(answer) == length + 1:
                return True, answer
            else:
                 return False, answer
        for dest in visit[begin]:
            if visit[begin][dest] > 0:
                visit[begin][dest] -= 1
                flag, result = found(dest, visit, answer + [dest])
                if flag:
                    return True, result
                visit[begin][dest] += 1

        return False, answer
    
    
    _, answer = found("ICN", visit, ["ICN"])
    return answer


if solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"]:
    print('Success')
else:
    print('Fail')

if solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]:
    print('Success')
else:
    print('Fail')

if solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"], ["AAA", "DDD"], ["AAA","CCC"], ["DDD", "AAA"]]) == ["ICN", "BBB", "ICN", "AAA", "DDD", "AAA", "CCC"]:
    print('Success')
else:
    print('Fail')

if solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "AOO"], ["AOO", "ICN"], ["ICN", "AOO"]]) == ["ICN", "AOO", "BOO", "AOO", "ICN", "AOO"]:
    print('Success')
else:
    print('Fail')


# 다른사람의 풀이중 제일 이상적인 풀이
from collections import defaultdict
def solution(tickets):
    r = defaultdict(list)
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        print(s, p, q)
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]

if solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"]:
    print('Success')
else:
    print('Fail')

if solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]:
    print('Success')
else:
    print('Fail')

if solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"], ["AAA", "DDD"], ["AAA","CCC"], ["DDD", "AAA"]]) == ["ICN", "BBB", "ICN", "AAA", "DDD", "AAA", "CCC"]:
    print('Success')
else:
    print('Fail')

if solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "AOO"], ["AOO", "ICN"], ["ICN", "AOO"]]) == ["ICN", "AOO", "BOO", "AOO", "ICN", "AOO"]:
    print('Success')
else:
    print('Fail')