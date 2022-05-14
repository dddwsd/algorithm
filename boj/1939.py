'''
n개의 섬으로 이루어진 나라

몇개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업 - 두개의 섬에 공장을 세워 물품을 생산하는 일

물품을 생산하다 보면 공장에서 다른 공장으로 생산중이던 물품을 수송해야 할 일이 생긴다.

각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다.

중량제한 초과하면 다리 무너짐

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램
'''
# binary search
from collections import defaultdict
from collections import deque
n,m = map(int,input().split())

bridge = defaultdict(list)
_min = 1000000000
_max = 1
for _ in range(m):
    a,b,c = map(int,input().split())
    
    bridge[a].append([b,c])
    bridge[b].append([a,c])
    _min = min(_min,c)
    _max = max(_max,c)
land1,land2 = map(int,input().split())
result = -1

def bfs(_max):
    q = deque([land1])
    visited = [False] * (n+1)
    visited[land1] = True
    
    while q:
        s = q.popleft()
        for d, val in bridge[s]:
            if not visited[d] and val >= _max:
                q.append(d)
                visited[d] = True
    return visited[land2]

while _min <= _max:
    mid = (_min + _max)//2
    if bfs(mid):
        result = mid
        _min = mid+1
    else:
        _max = mid-1
print(result)
