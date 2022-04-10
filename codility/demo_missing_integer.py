# https://app.codility.com/demo/take-sample-test/

# 차집합을 이용한 풀이
def solution(A):
    integer = [idx for idx in range(1, len(A)+2)]
    diff = set(integer) - set(A)
    return min(diff)

# 단순 for loop
def solution(A):
    A = set(A)
    for idx in range(1, 100002):
        if idx not in A:
            return idx


A = [1, 2, 6 ,4 ,3, 8]
result = 5
if solution(A) == result:
    print('Success')
else:
    print('Fail')

A = [-2, -1]
result = 1
if solution(A) == result:
    print('Success')
else:
    print('Fail')

A = [1, 2, 3]
result = 4
if solution(A) == result:
    print('Success')
else:
    print('Fail')