# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import defaultdict
from collections import deque
def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for line in edge:
        p1, p2 = line
        graph[p1].append(p2)
        graph[p2].append(p1)
    
    visit = [False for _ in range(n+1)]
    visit[0] = True
    line = deque([1])
    cnt = 0
    while True:
        temp = deque()
        while line:    
            point = line.popleft()
            visit[point] = True
            for end in graph[point]:
                if visit[end]:
                    continue
                visit[end] = True
                temp.append(end)
        if set(visit) == set([True]):
            answer = len(temp)
            break
        line = temp

    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
result = 3
if solution(n, edge) == result:
    print('Success')
else:
    print('Fail')

# 다른 사람의 좋은 풀이
def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for line in edge:
        p1, p2 = line
        graph[p1-1].append(p2-1)
        graph[p2-1].append(p1-1)
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = deque([0])
    is_visit[0] = True

    while queue:
        start = queue.popleft()

        for end in graph[start]:
            if is_visit[end] == False:
                is_visit[end] = True
                queue.append(end)
                distances[end] = distances[start] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
result = 3
if solution(n, edge) == result:
    print('Success')
else:
    print('Fail')