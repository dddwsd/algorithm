# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    # answer의 최소값이 8보다 크면 -1을 리턴
    answer = -1
    result = {1: set([N])}
    if N == number:
        return 1
    else:
        # N을 3번 사용해서 만들 수 있는 값
        # # N을 3번 이어붙인 경우
        # # (N을 1번 사용해서 만들 수 있는값)과 (N을 2번 사용해서 만들 수 있는 값)의 사칙연산 결과
        # # (N을 2번 사용해서 만들 수 있는값)과 (N을 1번 사용해서 만들 수 있는 값)의 사칙연산 결과
        for n in range(2, 9):
            val = int(f'{N}'*n)
            if val == number:
                return n
            values = set([val])
            # 사칙연산들
            for i in range(1, n):
                for item1 in result[i]:
                    for item2 in result[n-i]:
                        val = item1 + item2
                        values.add(val)
                        val = item1 - item2
                        values.add(val)
                        val = item1 * item2
                        values.add(val)
                        if item2 != 0:
                            val = item1 // item2
                            values.add(val)
            if number in values:
                return n
            result[n] = values
    return answer

N = 5
number = 12
result = 4
if solution(N, number) == result:
    print('Success')
else:
    print('Fail')

N = 2
number = 11
result = 3
if solution(N, number) == result:
    print('Success')
else:
    print('Fail')

