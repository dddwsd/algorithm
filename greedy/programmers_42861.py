# https://programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = 0
    dic = {}
    points = [i for i in range(n-1, -1, -1)]

    for cost in costs:
        b1, b2, val = cost
        if b1 not in dic:
            dic[b1] = {}
        if b2 not in dic:
            dic[b2] = {}
        dic[b1][b2] = val
        dic[b2][b1] = val

    points = [0]
    while len(points) != n:
        edges = []
        for point in points:
            edges.extend(dic[point].items())
        edges = sorted(edges, key=lambda x:x[1])
        for dest, val in edges:
            if dest not in points:
                points.append(dest)
                answer += val
                break

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
result = 4
if solution(n, costs) == result:
    print('Success')
else:
    print('Fail')