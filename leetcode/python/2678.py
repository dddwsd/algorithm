"""
2678 - Number of Senior Citizens
"""
from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for detail in details:
            age = detail[11:13]
            if int(age) > 60:
                result += 1
        return result


solution = Solution()
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
output = 2
if solution.countSeniors(details) == output:
    print('Success')
else:
    print('Fail')
