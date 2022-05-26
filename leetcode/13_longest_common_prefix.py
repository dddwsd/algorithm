# https://leetcode.com/problems/longest-common-prefix/

from typing import List

# 41ms
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x: len(x))
        answer = len(strs[0])
        dic = {}
        for string in strs:
            for idx in range(0, answer):
                if idx not in dic:
                    dic[idx] = set([string[idx]])
                else:
                    if string[idx] not in dic[idx]:
                        answer = idx
                        break
        return strs[0][:answer]

# 53ms
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for word in strs:
            while (common != word[0:len(common)]):
                common = common[0:len(common)-1]
        return common    


solution = Solution()
strs = ["flower","flow","flight"]
output = 'fl'
if solution.longestCommonPrefix(strs) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
strs = ["dog","racecar","car"]
output = ''
if solution.longestCommonPrefix(strs) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
strs = ["ab", "a"]
output = 'a'
if solution.longestCommonPrefix(strs) == output:
    print('Success')
else:
    print('Fail')
