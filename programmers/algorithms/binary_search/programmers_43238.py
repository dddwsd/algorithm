# https://programmers.co.kr/learn/courses/30/lessons/43238


# 총 걸린시간을 binary search의 기준으로 찾아가는게 핵심.
def solution(n, times):
    answer = 0
    # 가장 빠른 경우 = 심사관의 수 > 사람
    # 가장 느린 경우 = 가장 느린 심사관에 모든 사람이 지나가는경우 - 실제로 이런 경우는 없음 그냥 최대값 설정 위함
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

n = 6
times = [7, 10]
result = 28
if solution(n, times) == result:
    print('Success')
else:
    print('Fail')
