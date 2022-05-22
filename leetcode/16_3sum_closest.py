
from typing import List

# in-out
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        closest = 10 ** 9
        for mid in range(1, length-1):
            left = mid - 1
            right = mid + 1
            while left >= 0 and right < length:
                diff = nums[left] + nums[mid] + nums[right] - target
                if diff == 0:
                    return target
                elif diff > 0:
                    if abs(diff) < abs(target - closest):
                        closest = nums[left] + nums[mid] + nums[right]
                    left -= 1
                    while left >= 0 and nums[left] == nums[left+1]:
                        left -= 1
                elif diff < 0:
                    if abs(diff) < abs(target - closest):
                        closest = nums[left] + nums[mid] + nums[right]
                    right += 1
                    while right < length and nums[right-1] == nums[right]:
                        right += 1
        return closest

# out-in
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        closest = 10 ** 9
        for mid in range(1, length-1):
            left = 0
            right = length - 1
            while left < mid and mid < right:
                diff = nums[left] + nums[mid] + nums[right] - target
                if diff == 0:
                    return target
                elif diff < 0:
                    if abs(diff) < abs(target - closest):
                        closest = nums[left] + nums[mid] + nums[right]
                    left += 1
                    while left < mid and nums[left] == nums[left-1]:
                        left += 1
                elif diff > 0:
                    if abs(diff) < abs(target - closest):
                        closest = nums[left] + nums[mid] + nums[right]
                    right -= 1
                    while mid < right and nums[right] == nums[right+1]:
                        right -= 1
        return closest


solution = Solution()
nums = [-1, 2, 1, -4]
target = 1
output = 2
if solution.threeSumClosest(nums, target) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [0, 0, 0]
target = 1
output = 0
if solution.threeSumClosest(nums, target) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [1, 1, 1, 0]
target = 100
output = 3
if solution.threeSumClosest(nums, target) == output:
    print('Success')
else:
    print('Fail')