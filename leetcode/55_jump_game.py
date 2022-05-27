# https://leetcode.com/problems/jump-game/

from typing import List

# 966ms
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 현재위치에서 갈 수 있는 거리가 있고
        # 
        end = 0
        max_jump = 0

        for idx in range(len(nums)-1):
            max_jump = max(max_jump, idx + nums[idx])
            if idx == end:
                end = max_jump

        if end < len(nums) - 1:
            return False
        return True

# 478ms
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) -1

        for idx in range(len(nums)-1, -1, -1):
            if idx + nums[idx] >= end:
                end = idx
        return end == 0


solution = Solution()
nums = [2, 3, 1, 1, 4]
output = True
if solution.canJump(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [3, 2, 1, 0, 4]
output = False
if solution.canJump(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [0]
output = True
if solution.canJump(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [0, 2, 3]
output = False
if solution.canJump(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [2, 0]
output = True
if solution.canJump(nums) == output:
    print('Success')
else:
    print('Fail')