# https://leetcode.com/problems/regular-expression-matching/

# 정규표현식 사용
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.fullmatch(p, s):
            return True
        return False

solution = Solution()
s = 'aa'
p = 'a'
output = False
if solution.isMatch(s, p) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = 'aa'
p = 'aa'
output = True
if solution.isMatch(s, p) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = 'ab'
p = '.*'
output = True
if solution.isMatch(s, p) == output:
    print('Success')
else:
    print('Fail')

# 정규표현식 사용 x
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.fullmatch(p, s):
            return True
        return False

solution = Solution()
s = 'aa'
p = 'a'
output = False
if solution.isMatch(s, p) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = 'aa'
p = 'aa'
output = True
if solution.isMatch(s, p) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = 'ab'
p = '.*'
output = True
if solution.isMatch(s, p) == output:
    print('Success')
else:
    print('Fail')


