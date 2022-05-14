# https://programmers.co.kr/learn/courses/30/lessons/42860
# greedy로 분류되어 있는데 greedy로 풀 수 없음..

from collections import deque
def solution(name):
    answer = 20*26*5
    name = list(name)
    length = len(name)
    result = deque([[0, 1, length-1, 0, 'A' * length]])
    
    while result:
        cur, post, pre, val, base = result.popleft()
        base = list(base)
        # 알파벳 설정
        start, end = base[cur], name[cur]
        up = abs(ord(end) - ord(start))
        down = abs(ord('Z') - ord(end) + 1)
        val += min(up, down)
        base[cur] = end

        if base == name:
            answer = min(val, answer)
            continue

        # 커서 정하기
        while name[post] == 'A':
            post += 1
        while name[pre] == 'A':
            pre -= 1

        if 0 <= cur < post:
            right = post - cur
            left = cur + length - pre
        else:
            right = length - cur + post
            left = cur - pre

        # 왼쪽 저장
        result.append([pre, post, pre-1, val + left, ''.join(base)])
        # 오른쪽 저장
        result.append([post, post+1, pre, val + right, ''.join(base)])

    return answer

name = "JAN"
result = 23
if solution(name) == result:
    print('Success')
else:
    print('Fail')

name = "JEROEN"
result = 56
if solution(name) == result:
    print('Success')
else:
    print('Fail')

name = "ABAABB"
result = 7
if solution(name) == result:
    print('Success')
else:
    print('Fail')

name = "AABAAABAAAB"
result = 11
if solution(name) == result:
    print('Success')
else:
    print('Fail')

name = "AAAA"
result = 0
if solution(name) == result:
    print('Success')
else:
    print('Fail')

name = "BBAAABB"
result = 8
if solution(name) == result:
    print('Success')
else:
    print('Fail')

name = "BBBBAAAABA"
result = 12
if solution(name) == result:
    print('Success')
else:
    print('Fail')

# 다른 사람의 풀이
def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    # 알파벳 업다운 미리 계산.
    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        # 다음 위치 설정
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        # idx면 오른쪽으로 갔다가 왼쪽으로 간 경우
        # n-next_idx면 왼쪽으로 갔다가 오른쪽으로 간경우.
        # 둘 중 더 짧은 경우를 택한다.
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer

name = "BBAB"
result = 6
if solution(name) == result:
    print('Success')
else:
    print('Fail')
