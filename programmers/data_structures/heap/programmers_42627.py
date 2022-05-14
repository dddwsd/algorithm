# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq
def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x:(x[0],x[1]))
    # 무조건 짧은거 먼저.
    waits = []
    cur = -1
    for job in jobs:
        start, cur_val = job
        # job의 시작시간이 현재 진행중인 job의 종료시간보다 빨라서 대기해야 하는 경우
        if cur > start:
            answer += cur - start
            heapq.heappush(waits, cur_val)
        # job의 시작시간이 현재 진행중인 job의 종료시간 보다 뒤인 경우
        # 현재 waits에 있는 것들중에서 짧은 것부터 실행시키면서 job의 종료시간을 뒤로 미룸
        # 미루다가 만약 job의 종료시간보다 빨라지면 heapq에 넣고 다시 종료
        else:
            while waits:
                val = heapq.heappop(waits)
                answer += val * (len(waits) + 1)
                cur += val
                if start < cur:
                    answer += cur - start
                    heapq.heappush(waits, cur_val)
                    break
        
        # 진행중인게 없는 경우
        if cur <= start:
            cur = start + cur_val
            answer += cur_val

    while waits:
        val = heapq.heappop(waits)
        answer += val * (len(waits) + 1)
        cur += val

    return answer // n

jobs = [[0, 3], [1, 9], [2, 6]]
result = 9
if solution(jobs) == result:
    print('Success')
else:
    print('Fail')

jobs = [[16, 5], [0, 3], [1, 9], [2, 6]]
result = 8
if solution(jobs) == result:
    print('Success')
else:
    print('Fail')

jobs = [[20, 5], [0, 3], [1, 9], [2, 6]]
result = 8
if solution(jobs) == result:
    print('Success')
else:
    print('Fail')

# 다른 사람 풀이
import heapq

def solution(jobs):
    tasks = sorted([(x[1], x[0]) for x in jobs],
                   key=lambda x: (x[1], x[0]), reverse=True)
    q = []
    heapq.heappush(q, tasks.pop())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[-1][1] <= current_time:
            heapq.heappush(q, tasks.pop())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.pop())
    return total_response_time // len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
result = 9
if solution(jobs) == result:
    print('Success')
else:
    print('Fail')

jobs = [[16, 5], [0, 3], [1, 9], [2, 6]]
result = 8
if solution(jobs) == result:
    print('Success')
else:
    print('Fail')

jobs = [[20, 5], [0, 3], [1, 9], [2, 6]]
result = 8
if solution(jobs) == result:
    print('Success')
else:
    print('Fail')