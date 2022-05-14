# https://programmers.co.kr/learn/courses/30/lessons/43162

# Result
"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.11ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10MB)
테스트 8 〉	통과 (0.08ms, 10.2MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.2MB)
테스트 11 〉	통과 (0.34ms, 10.4MB)
테스트 12 〉	통과 (0.49ms, 10.1MB)
테스트 13 〉	통과 (0.17ms, 10.3MB)
"""

# 0번 컴퓨터에서 시작해서 갈 수 있는 모든 컴퓨터 체킹
# 남아있는 컴퓨터들 중에 방문하지 않은 곳이 있다면, 그 컴퓨터 부터 다시 시작
def solution(n, computers):
    answer = 0
    visit = [False for _ in range(n)]

    while not (len(set(visit)) == 1 and list(set(visit))[0] == True):
        idx =  visit.index(False)
        def found(idx):
            visit[idx] = True
            adjacent = computers[idx]
            for idx, item in enumerate(adjacent):
                if item == 1 and visit[idx] == False:
                    found(idx)
        found(idx)
        answer += 1
    return answer

if solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2:
    print('Success')
else:
    print('fail')

if solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1:
    print('Success')
else:
    print('fail')