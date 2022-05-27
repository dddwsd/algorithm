# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len + s2_len != s3_len:
            return False
        dp = [ [False for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]
        dp[0][0] = True
        for y in range(1, s1_len+1):
            dp[y][0] = dp[y-1][0] and s1[y-1] == s3[y-1]
        for x in range(1, s2_len+1):
            dp[0][x] = dp[0][x-1] and s2[x-1] == s3[x-1]
        for y in range(1, s1_len+1):
            for x in range(1, s2_len+1):
                dp[y][x] = (dp[y-1][x] and s1[y-1] == s3[y-1+x]) or (dp[y][x-1] and s2[x-1] == s3[y-1+x])
        return dp[s1_len][s2_len]

solution = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
if solution.isInterleave(s1, s2, s3):
    print('Success')
else:
    print('Fail')
