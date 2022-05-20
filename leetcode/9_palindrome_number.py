# https://leetcode.com/problems/palindrome-number/

# 54ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse = x[::-1]
        if x == reverse:
            return True
        return False

# 58ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        start = 0
        end = len(x) - 1
        while start <= end:
            if x[start] != x[end]:
                return False
            start += 1
            end -= 1
        return True

  
solution = Solution()
x = 121
output = True
if solution.isPalindrome(x) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
x = -121
output = False
if solution.isPalindrome(x) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
x = 10
output = False
if solution.isPalindrome(x) == output:
    print('Success')
else:
    print('Fail')