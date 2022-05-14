# https://programmers.co.kr/learn/courses/30/lessons/43163

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있다
# 2. words에 있는 단어로만 변환할 수 있다.
from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    # words를 돌면서 알파벳 한개만 다른거 확인
    # 이전에 방문했었는지 체크
    # 들어가기
    visit = {}
    for word in words:
        visit[word] = False
    
    bfs = deque()
    bfs.append((begin, visit, answer))

    def compare(cur, word):
        diff = 0
        for a, b in zip(cur, word):
            if a != b:
                diff += 1
        if diff == 1:
            return True
        return False

    while bfs:
        cur, visit, answer = bfs.popleft()
        answer += 1
        for word, boolean in visit.items():
            if boolean == False and compare(cur, word):
                visit[word] = True
                if word == target:
                    return answer
                bfs.append([word, visit, answer])
    return 0

if solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == 4:
    print(f'Success')
else:
    print('Fail')

if solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']) == 0:
    print(f'Success')
else:
    print('Fail')

if solution('hit', 'hhh', ['hhh', 'hht']) == 2:
    print(f'Success')
else:
    print('Fail')