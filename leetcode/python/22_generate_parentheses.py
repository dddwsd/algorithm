# https://leetcode.com/problems/generate-parentheses/

from typing import List

import collections

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        parentheses = collections.deque([['', n, n]])
        while parentheses:
            val, left, right = parentheses.popleft()
            if left == 0 and right == 0:
                answer.append(val)
                continue

            if left:
                parentheses.append([val + '(', left-1, right])
            
            if right and left < right:
                parentheses.append([val + ')', left, right-1])
        return answer


solution = Solution()
n = 3
output = ["((()))","(()())","(())()","()(())","()()()"]
if solution.generateParenthesis(n) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
n = 1
output = ["()"]
if solution.generateParenthesis(n) == output:
    print('Success')
else:
    print('Fail')