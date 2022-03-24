# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):

    answer = 1
    cur = 0
    new = 0
    length = len(truck_weights)
    rest = [bridge_length for _ in truck_weights]

    # for loop 안에 n초에 일어나는 일을 적음.
    # 마지막꺼만 남으면 나가서 걍 남은 초 다더해주고 끝
    while new < length:
        # new를 올릴 수 있는가?
        if sum(truck_weights[cur:new+1]) <= weight:
            # 올릴 수 있다 -> 올림
            new += 1
        else:
            # 올릴 수 없다.
            # cur에 있는게 1초 남을 때 까지 시간 워프
            warp = rest[cur] - 1
            answer += warp
            for idx in range(cur, new):
                rest[idx] -= warp
        # 1초가 흐름 -> 
        for idx in range(cur, new):
            rest[idx] -= 1
        answer += 1
        if rest[cur] <= 0:
            cur += 1
    return answer + rest[-1]

if solution(2, 10, [7, 4, 5, 6]) == 8:
    print('Success')
else:
    print('Fail')

if solution(100, 100, [10]) == 101:
    print('Success')
else:
    print('Fail')

if solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) == 110:
    print('Success')
else:
    print('Fail')