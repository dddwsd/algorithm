# https://leetcode.com/problems/valid-parentheses/

# 62ms
class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        dic = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        for item in s:
            if item in ['(', '[', '{']:
                queue.append(item)
            else:
                if not queue:
                    return False
                val = queue.pop()
                if dic[val] != item:
                    return False
        if queue:
            return False
        return True

# 47ms
class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        dic = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for item in s:
            if item in ['(', '[', '{']:
                queue.append(item)
            else:
                if queue and dic[item] == queue[-1]:
                    queue.pop()
                else:
                    return False
        return True if not queue else False
        

solution = Solution()
s = "()"
output = True
if solution.isValid(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = "()[]{}"
output = True
if solution.isValid(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = "(]"
output = False
if solution.isValid(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = "("
output = False
if solution.isValid(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = ")"
output = False
if solution.isValid(s) == output:
    print('Success')
else:
    print('Fail')