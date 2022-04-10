# https://app.codility.com/programmers/trainings/1/slalom_skiing/start/


# slalom - 내리막길 + 양쪽에 장벽
# 장벽은 slope 상단에 위치한 출발선에 수직
# 트랙에는 n개의 slalom gate가 있음
# 각 게이트는 출발선과 오른쪽 장벽을 기준으로 거리에 배치
# 출발선의 아무곳에서나 스키를 타고 최대한 많은 게이트를 통과한 후 슬로프 하단에서 slalom 마침
# 왼쪽 or 오른쪽으로 스키 탈 수 있음
# 왼쪽으로 타면 오른쪽 방벽에서 멀어지는 거리의 게이트를 통과하고 
# 오른쪽으로 타면 오른쪽 방벽에 가까워지는 거리의 게이트를 통과한다
# 방향 변경 최대 2번
# 통과할 수 있는 게이트 최대수
from collections import deque
def solution(A):
    answer = 0
    # slalom은 현재까지 지나온 슬라롬의 정보를 담고있는 deque
    # 구성은 다음과 같다 [현재 지나온 gate수, 이전 게이트의 index, 현재 방향, 방향회전 횟수]
    # 방향은 'left', 'rifgt'로 나뉜다.
    slalom = deque()
    length = len(A)
    # 모든 점을 지남.
    for idx, cur in enumerate(A):
        # 현재 deque의 있는 것들에 대해 현재 게이트를 지날지 말지 정함
        for _ in range(len(slalom)):
            gate_num, before_idx, direc, direc_num = slalom.popleft()
            if length - 1 - idx + gate_num <= answer:
                continue
            # 이전게이트 대비 현재 게이트의 방향.
            cur_direc = cur - A[before_idx]

            if cur_direc < 0:
                cur_direc = 'left'
            else:
                cur_direc = 'right'


            # 방향이 같은 경우
            if cur_direc == direc:
                # # 가거나
                answer = max(answer, gate_num+1)
                slalom.append([gate_num+1, idx, cur_direc, direc_num])

                # # 현재점과 이전점 사이에 점들이 존재할 경우 반대방향을 가지 않은 것이기에 또 기다릴 수 없음
                if idx-1 == before_idx:
                    # # 가지않고 다음에 반대 방향이 있을때까지 기다리거나 -> 대신 다음에 반대방향 나오면 무조건 가야함.
                    slalom.append([gate_num, before_idx, direc, direc_num])
            # 방향이 다른 경우
            else:
                # 방향 이동을 할 수 있으면 
                if direc_num:
                    # 가거나
                    answer = max(answer, gate_num+1)
                    slalom.append([gate_num+1, idx, cur_direc, direc_num-1])

                # 같은 방향이 나오기 까지 기다리거나
                slalom.append([gate_num, before_idx, direc, direc_num])

        # 남은 점의 개수가 현재 answer보다 작으면 시작점이 될 수 없음.
        if length - 1 - idx >= answer:
            slalom.append([1, idx, 'left', 2])
            slalom.append([1, idx, 'right', 2])

    return answer
            




A = [15, 13, 5, 7, 4, 10, 12, 8, 2, 11, 6, 9, 3]
result = 8
if solution(A) == result:
    print('Success')
else:
    print('Fail')

A = [1, 5]
result = 2
if solution(A) == result:
    print('Success')
else:
    print('Fail')