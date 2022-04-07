# https://leetcode.com/problems/two-sum/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return[i, j]

solution = Solution()
nums = [2, 7, 11, 15]
target = 9
output = [0, 1]
if solution.twoSum(nums, target) == output:
    print('Success')
else:
    print('Fail')

# two point algorithm
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = {}
        for i, num in enumerate(nums):
            if num in left:
                return [left[num], i]
            else:
                left[target-num] = i

solution = Solution()
nums = [2, 7, 11, 15]
target = 9
output = [0, 1]
if solution.twoSum(nums, target) == output:
    print('Success')
else:
    print('Fail')
