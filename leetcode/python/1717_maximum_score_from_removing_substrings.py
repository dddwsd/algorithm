"""
Runtime
6573 ms / Beats 5.03%

Memory
17.58 MB / Beats 77.99%
"""
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def get_score(string, substring, score, current_score):
            length = len(string)
            reduce_s = string.replace(substring, "")
            return reduce_s, current_score + ((length - len(reduce_s)) // 2) * score

        if x > y :
            large = x
            large_sub = "ab"
            small = y
            small_sub = "ba"
        else:
            large = y
            large_sub = "ba"
            small = x
            small_sub = "ab"

        current_score = 0
        while True:
            length = len(s)
            s, current_score = get_score(s, large_sub, large,  current_score)
            if length == len(s):
                break

        while True:
            length = len(s)
            s, current_score = get_score(s, small_sub, small,  current_score)
            if length == len(s):
                break

        return current_score

"""
Runtime
300 ms / Beats 55.98%

Memory
18.53 MB / 22.64%
"""
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y :
            large = x
            large_sub = "ab"
            small = y
            small_sub = "ba"
        else:
            large = y
            large_sub = "ba"
            small = x
            small_sub = "ab"

        score = 0
        remain_s = list()
        for char in s:
            if remain_s and remain_s[-1] + char == large_sub:
                score += large
                remain_s.pop()
            else:
                remain_s.append(char)

        temp = list()
        for char in remain_s:
            if temp and temp[-1] + char == small_sub:
                score += small
                temp.pop()
            else:
                temp.append(char)

        return score

"""
Runtime
251 ms / Beats 66.04%

Memory
18.48 MB / 32.08%
"""

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y :
            large = x
            large_sub = "ab"
            small = y
            small_sub = "ba"
        else:
            large = y
            large_sub = "ba"
            small = x
            small_sub = "ab"

        score = 0
        remain_s = list()
        for char in s:
            if remain_s and remain_s[-1] == large_sub[0] and char == large_sub[1]:
                score += large
                remain_s.pop()
            else:
                remain_s.append(char)

        temp = list()
        for char in remain_s:
            if temp and temp[-1] == small_sub[0] and  char == small_sub[1]:
                score += small
                temp.pop()
            else:
                temp.append(char)

        return score



solution = Solution()
s = "aabbaaxybbaabb"
x = 5
y = 4
output = 20
if solution.maximumGain(s) == output:
    print('Success')
else:
    print('Fail')
