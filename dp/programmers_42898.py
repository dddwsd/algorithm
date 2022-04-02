# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    for x, y in puddles:
        dp[y-1][x-1] = -1
    dp[0][0] = 1
    
    for x in range(m):
        for y in range(n):
            # 우물은 건너뜀
            if dp[y][x] == -1:
                continue
            # 왼쪽
            if 0 <= x-1 and dp[y][x-1] != -1:
                dp[y][x] += dp[y][x-1]
            # 위
            if 0<= y-1 and dp[y-1][x] != -1:
                dp[y][x] += dp[y-1][x]

    return dp[-1][-1] % 1000000007
    
    
        

m = 4
n = 3
puddles = [[2, 2]]
result = 4
if solution(m, n, puddles) == result:
    print('Success')
else:
    print('Fail')

