# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, K):
    answer = 0
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + 두 번째로 맵지 않은 음식의 스코빌 지수 * 2
    heapq.heapify(scoville)
    # 계속 len 구하면 시간 오래 걸리니 미리 구하기
    length = len(scoville)
    while scoville[0] < K:
        first = heapq.heappop(scoville)
        length -= 1
        if length >= 1:
            second = heapq.heappop(scoville)
            length -= 1
        elif length == 0:
            second = 0
        
        new = first + second * 2
        if new < K:
            if not scoville:
                return -1
        heapq.heappush(scoville, new)
        length += 1
        answer += 1
            
    return answer

scoville = [3, 1, 2, 9, 10, 12]
K = 7
result = 2
if solution(scoville, K) == result:
    print('Success')
else:
    print('Fail')