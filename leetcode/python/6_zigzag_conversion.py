# https://leetcode.com/problems/zigzag-conversion/

# 1 2 3 4 5 4 3 2 
# 1 2 3 4 3 2  
# 1 2 3 2

# numRows * 2 - 2 가 1 cycle 
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ''
        interval = numRows * 2 - 2
        length = len(s)
        if interval == 0:
            return s
        cycles = length // interval
        for idx in range(numRows):
            for cycle in range(cycles+2):
                before = cycle * interval - idx
                after = cycle * interval + idx
                if idx == 0 or idx == numRows-1:
                    if after < length:
                        answer += s[after]
                else:
                    if 0 <= before and before < length:
                        answer += s[before]
                    if 0 <= after and after < length:
                        answer += s[after]
        return answer

solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
output =  "PAHNAPLSIIGYIR"
if solution.convert(s, numRows) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = "PAYPALISHIRING"
numRows = 4
output =  "PINALSIGYAHRPI"
if solution.convert(s, numRows) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = "A"
numRows = 1
output =  "A"
if solution.convert(s, numRows) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = "ABCDE"
numRows = 4
output =  "ABCED"
if solution.convert(s, numRows) == output:
    print('Success')
else:
    print('Fail')