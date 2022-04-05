# https://programmers.co.kr/learn/courses/30/lessons/43236

# goal = 거리의 최소값
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left, right, = 0, distance
    while left <= right:
        mid = (left + right) // 2
        remove = 0
        cur = 0
        # 거리의 최소값이 mid일 때, 지워지는 바위의 수가 n이 맞는지 확인.
        for rock in rocks:
            if rock - cur < mid:
                remove += 1
            else:
                cur = rock
            if remove > n:
                break
        if remove > n:
            right = mid - 1
        # 지워지는 바위의 수가 n일 경우 answer로 설정하고
        # 더 큰 값중에서 지워지는 바위의 수가 n개가 있는지 확인.
        else:
            answer = mid
            left = mid + 1

    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
result = 4
if solution(distance, rocks, n) == result:
    print('Success')
else:
    print('Fail')