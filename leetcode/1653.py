"""
1653. Minimum Deletions to Make String Balanced
"""

"""
Runtime
276ms / 63.67%
Memory
17.64MB / 79.00%
"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        start_idx = 0
        end_idx = len(s)-1
        while start_idx < end_idx:
            if s[start_idx] == "a":
                start_idx += 1
            if s[end_idx] == "b":
                end_idx -= 1
            if s[start_idx] == "b" and s[end_idx] == "a":
                break

        result = 0
        cur_a = 0
        remove_a = 0
        cur_b = 0
        for idx in range(start_idx, end_idx+1):
            if s[idx] == "a":
                cur_a += 1
            if s[idx] == "b":
                if cur_a:
                    if remove_a + cur_a >= cur_b:
                        remove_a = 0
                        result += cur_b
                        cur_b = 0
                        cur_a = 0
                    else:
                        remove_a += cur_a
                        cur_a = 0
                cur_b += 1

        if remove_a + cur_a >= cur_b:
            result += cur_b
        else:
            result += remove_a + cur_a
        return result


solution = Solution()
s = "aabbbb"
output = 0
if solution.minimumDeletions(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = "bbbaabbbbaaaaaaaaaaaa"
output = 7
if solution.minimumDeletions(s) == output:
    print('Success')
else:
    print('Fail')


solution = Solution()
s = "aababbab"
output = 2
if solution.minimumDeletions(s) == output:
    print('Success')
else:
    print('Fail')
