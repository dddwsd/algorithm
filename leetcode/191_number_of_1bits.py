# https://leetcode.com/problems/number-of-1-bits/

# 50ms
class Solution:
    def hammingWeight(self, n: int) -> int:
        n_str = "{0:b}".format(n)
        return n_str.count('1')

# 39ms
class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n // (2**num):
            num += 1
        
        answer = 0
        for digits in range(num, -1, -1):
            if n // (2**digits):
                n -= 2**digits
                answer += 1

        return answer


solution = Solution()
n =  11
output = 3
if solution.hammingWeight(n) == output:
    print('Success')
else:
    print('Fail')
