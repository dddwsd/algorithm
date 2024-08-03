# https://leetcode.com/problems/count-and-say/

# 39ms
class Solution:
    def countAndSay(self, n: int) -> str:
        a = '1'
        for _ in range(n-1):
            num = 0
            before = a[0]
            result = ''
            for item in a:
                if item == before:
                    num += 1                    
                else:
                    result += f'{num}{before}'
                    before = item
                    num = 1
            result += f'{num}{before}'
            a = result
        return a


solution = Solution()
n = 1
output = '1'
if solution.countAndSay(n) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
n = 4
output = '1211'
if solution.countAndSay(n) == output:
    print('Success')
else:
    print('Fail')