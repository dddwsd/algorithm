"""
1460 - Make Two Arrays Equal by Reversing Subarrays
"""
from typing import List

"""
Runtime
74ms / 58.36%
Memory
16.70 / 88.16%
"""
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target == arr

"""
Runtime
74ms / 58.36%
Memory
16.87MB / 22.18%
"""
from collections import defaultdict
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_dict = defaultdict(int)
        for target_item, arr_item in zip(target, arr):
            target_dict[target_item] += 1
            target_dict[arr_item] -= 1
        return set([0]) == set(target_dict.values())


solution = Solution()
target = [1,2,3,4]
arr = [2,4,1,3]
outputs = True
if solution.canBeEqual(target, arr) == outputs:
    print("Success")
else:
    print("Fail")
