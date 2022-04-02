# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = triangle[0][0]
    
    for height in range(1, len(triangle)):
        for width, val in enumerate(triangle[height]):
            sum_val = 0
            if width > 0:
                sum_val = max(sum_val, val + triangle[height-1][width-1])
            if width < height:
                sum_val = max(sum_val, val + triangle[height-1][width])
            triangle[height][width] = sum_val
            answer = max(answer, sum_val)
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
result = 30
if solution(triangle) == result:
    print('Success')
else:
    print('Fail')
