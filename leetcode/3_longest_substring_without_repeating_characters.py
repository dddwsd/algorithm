# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        start, end = 0, 0
        while end < len(s):
            if s[end] in s[start:end]:
                start += 1
            else:
                end += 1
            answer = max(answer, end - start)
        return answer

s = "abcabcbb"
output = 3
solution = Solution()
if solution.lengthOfLongestSubstring(s) == output:
    print('Success')
else:
    print('Fail')

s = "bbbbbb"
output = 1
solution = Solution()
if solution.lengthOfLongestSubstring(s) == output:
    print('Success')
else:
    print('Fail')

s = "pwwkew"
output = 3
solution = Solution()
if solution.lengthOfLongestSubstring(s) == output:
    print('Success')
else:
    print('Fail')

s = ""
output = 0
solution = Solution()
if solution.lengthOfLongestSubstring(s) == output:
    print('Success')
else:
    print('Fail')

s = " "
output = 1
solution = Solution()
if solution.lengthOfLongestSubstring(s) == output:
    print('Success')
else:
    print('Fail')