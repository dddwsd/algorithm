"""
18 - 4Sum
"""
from typing import List
"""
Time Limit Exceeded
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums.sort()
        length = len(nums)
        for a_idx in range(length-3):
            for b_idx in range(a_idx+1, length-2):
                for c_idx in range(b_idx+1, length-1):
                    for d_idx in range(c_idx+1, length):
                        if nums[a_idx] + nums[b_idx] + nums[c_idx] + nums[d_idx] == target:
                            if (nums[a_idx], nums[b_idx], nums[c_idx], nums[d_idx]) not in result:
                                result.add((nums[a_idx], nums[b_idx], nums[c_idx], nums[d_idx]))
        return list(map(list, result))

"""
Time Limit Exceeded
"""
from itertools import combinations
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dup_check = set()
        result = []
        for com_nums in set(combinations(nums, 4)):
            sorted_list = sorted(com_nums)
            if sum(com_nums) == target and tuple(sorted_list) not in dup_check:
                result.append(sorted_list)
                dup_check.add(tuple(sorted_list))
        return result

"""
Two pointer except first element
Runtime
945ms / 9.53%
Memory
16.57MB / 61.39%
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        dup_check = set()
        for a_idx in range(length-3):
            a = nums[a_idx]
            for b_idx in range(a_idx+2, length-1):
                b = nums[b_idx]
                left = b_idx-1
                right = b_idx+1
                while left > a_idx and right < length:
                    c = nums[left]
                    d = nums[right]
                    if a+b+c+d == target and tuple([a, b, c, d]) not in dup_check:
                        result.append([a,b,c,d])
                        dup_check.add(tuple([a,b,c,d]))
                    if a+b+c+d < target:
                        right += 1
                    else:
                        left -= 1
        return result



solution = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
if solution.fourSum(nums, target) == output:
    print('Success')
else:
    print('Fail')
