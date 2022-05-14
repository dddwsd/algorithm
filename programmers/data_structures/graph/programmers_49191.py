# https://programmers.co.kr/learn/courses/30/lessons/49191

from collections import defaultdict
def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)

    for result in results:
        win, lose = result
        win_graph[lose].add(win)
        lose_graph[win].add(lose)

    for i in range(1, n+1):
        for winner in win_graph[i]:
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:
            win_graph[loser].update(win_graph[i])

    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
result = 2
if solution(n, results) == result:
    print('Success')
else:
    print('Fail')
