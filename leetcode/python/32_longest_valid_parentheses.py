# https://leetcode.com/problems/longest-valid-parentheses/

# dp solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp_table = [0] * len(s)
        for idx, char in enumerate(s):
            if idx and char == ')':
                if s[idx-1] == '(':
                    dp_table[idx] = dp_table[idx-2] + 2
                elif s[idx-1] == ')':
                    if idx >= dp_table[idx-1] + 1 and s[idx - dp_table[idx-1] - 1] == '(':
                        dp_table[idx] = dp_table[idx-1] + dp_table[idx - dp_table[idx-1] - 2] + 2
        if dp_table:
            return max(dp_table)
        return 0

# stack solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        stack = [-1]
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    answer = max(answer, idx - stack[-1])
        return answer

# left to right
# right to lefty
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def find_max(s, sep):
            count = 0
            answer = 0
            temp = 0
            for char in s:
                if char == sep:
                    count += 1
                else:
                    # 닫을 수 있을 때
                    if count:
                        count -= 1
                        temp += 2
                        # 완전히 닫히면
                        if not count:
                            answer = max(answer, temp)
                    # 닫을 수 없다면
                    else:
                        temp = 0
            return answer

        return max(find_max(s, '('), find_max(s[::-1], ')'))




solution = Solution()
s = '(()'
output = 2
if solution.longestValidParentheses(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = ')()())'
output = 4
if solution.longestValidParentheses(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = ''
output = 0
if solution.longestValidParentheses(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = '()(()'
output = 2
if solution.longestValidParentheses(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = ")()())()()("
output = 4
if solution.longestValidParentheses(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = "(()())"
output = 6
if solution.longestValidParentheses(s) == output:
    print('Success')
else:
    print('Fail')
