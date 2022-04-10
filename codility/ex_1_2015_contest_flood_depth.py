# https://app.codility.com/programmers/trainings/1/flood_depth/start/

# 호수의 가장 깊은 부분의 최대 깊이
# A에 들어있는 값은 암석 바닥 고도
# 저지대는 가능한 한 많은 물을 보유
def solution(A):
    # 파인 곳의 시작과 끝을 알아야 함.
    start = 0
    # 파인 곳의 최저 깊이를 알아야함
    min_depth = 1
    # 최대 깊이
    max_depth = 0

    for end, height in enumerate(A):
        # 현재 높이가 start 높이보다 낮은 경우
        if height < A[start]:
            # 현재 높이가 min_depth보다 낮은 경우 갱신
            if min_depth >= height:
                min_depth = height
            # 현재 높이가 min_depth보다 높은 경우 - 최대 깊이 갱신
            else:
                max_depth = max(max_depth, height - min_depth)
        # 현재 높이가 start 높이랑 같거나 높은 경우
        else :
            # 바로 옆에 붙어 있지 않은 경우
            if end - start > 1:
                # 옆에 붙어있지 않은 경우에만 max_depth 기록 비교
                max_depth = max(max_depth, A[start] - min_depth)
            # 이후 start가 바뀌니 현재를 start로 설정
            start = end
            min_depth = height
    return max_depth

A = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
result = 2
if solution(A) == result:
    print('Success')
else:
    print('Fail')

A = [1, 1, 1, 1]
result = 0
if solution(A) == result:
    print('Success')
else:
    print('Fail')

A = [5, 2, 2, 5]
result = 3
if solution(A) == result:
    print('Success')
else:
    print('Fail')

A = [1, 2, 3, 4]
result = 0
if solution(A) == result:
    print('Success')
else:
    print('Fail')