# https://programmers.co.kr/learn/courses/30/lessons/49190

from collections import defaultdict
def solution(arrows):
    answer = 0
    move = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    x, y = 0, 0
    visit = defaultdict(set)
    for arrow in arrows:
        # 거리 1짜리 사각형에 대각선으로 이어지는 경우 카운팅을 위해 거리를 2로 늘려서 카운티 되게 함
        for _ in range(2):
            dx, dy = move[arrow]
            nx = x + dx
            ny = y + dy
            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]:
                answer += 1
                visit[(x,y)].add((nx, ny))
                visit[(nx, ny)].add((x, y))
            elif (nx, ny) not in visit:
                visit[(x, y)].add((nx, ny))
                visit[(nx, ny)].add((x, y))
            x, y = nx, ny

    return answer

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
result = 3
if solution(arrows) == result:
    print('Success')
else:
    print('Fail')