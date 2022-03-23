# problem: https://programmers.co.kr/learn/courses/30/lessons/43165

# results
"""
테스트 1 〉	통과 (301.83ms, 10.1MB)
테스트 2 〉	통과 (206.17ms, 10.3MB)
테스트 3 〉	통과 (0.22ms, 9.96MB)
테스트 4 〉	통과 (0.12ms, 10MB)
테스트 5 〉	통과 (9.07ms, 10.2MB)
테스트 6 〉	통과 (0.40ms, 10.2MB)
테스트 7 〉	통과 (0.30ms, 10.1MB)
테스트 8 〉	통과 (3.96ms, 10.2MB)
"""

# numbers에 +, -를 접목하여 target을 만들수 있는 경우의 수 
def solution(numbers, target):
    answer = 0
    result = 0
    idx = 0
    def select_op(idx, target, result, count):
        if idx == len(numbers):
            if target == result:
                count += 1
            return count

        if sum(numbers[idx:]) < abs(target-result):
            return count

        val = numbers[idx]
        # +
        count = select_op(idx + 1, target, result + val, count)
        # -
        count = select_op(idx + 1, target, result - val, count)
        return count
    
    return select_op(idx, target, result, answer)

if solution([1, 1, 1, 1, 1], 3) == 5:
    print(f'Success')
else:
    print(f'Fail')

if solution([4, 1, 2, 1], 4) == 2:
    print(f'Success')
else:
    print(f'Fail')


# -------------------------------------------------
# 다른 사람의 풀이에서 찾은 이상적인 solution
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

if solution([1, 1, 1, 1, 1], 3) == 5:
    print(f'Success')
else:
    print(f'Fail')

if solution([4, 1, 2, 1], 4) == 2:
    print(f'Success')
else:
    print(f'Fail')
