from typing import List

"""
Runtime
92ms / 97.27%
Memory
17.13MB / 14.55
"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_heights = sorted(list(zip(names, heights)), key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], sorted_heights))


solution = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
output = ["Mary","Emma","John"]
if solution.sortPeople(names, heights) == output:
    print('Success')
else:
    print('Fail')
