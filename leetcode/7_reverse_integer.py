# https://leetcode.com/problems/reverse-integer/

from collections import deque
class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = -1 * x
        x = deque(str(x)[::-1])
        while not x[0]:
            x.popleft()
        if flag:
            x.appendleft('-')
        x = int(''.join(x))
        if x > 2**31 -1 or x < -1 * (2 ** 31):
            x = 0

        return x

solution = Solution()
x = 123
output = 321
if solution.reverse(x) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
x = -123
output = -321
if solution.reverse(x) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
x = 120
output = 21
if solution.reverse(x) == output:
    print('Success')
else:
    print('Fail')