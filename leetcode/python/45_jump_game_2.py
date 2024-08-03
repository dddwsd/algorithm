# https://leetcode.com/problems/jump-game-ii/

from typing import List

# 17649 ms - accept or time limit
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp_table = [0] * len(nums)
        # dp_table의 각 위치에는 자신의 위치까지 올 수 있는 최소의 수
        for idx, num in enumerate(nums):
            for jump in range(1, num+1):
                if idx+jump < len(nums) and dp_table[idx+jump]:
                    dp_table[idx + jump] = min(dp_table[idx+jump], dp_table[idx] + 1)
                elif idx+jump < len(nums) and not dp_table[idx+jump]:
                    dp_table[idx + jump] = dp_table[idx] + 1
        return dp_table[-1]

# 284 ms
class Solution:
    def jump(self, nums: List[int]) -> int:
        answer = 0
        end = 0
        max_jump = 0
        for idx in range(len(nums) - 1):
            max_jump = max(max_jump, idx + nums[idx])
            if idx == end:
                end = max_jump
                answer += 1
        return answer
        

solution = Solution()
nums = [2, 3, 1, 1, 4]
output = 2
if solution.jump(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [2, 3, 0, 1, 4]
output = 2
if solution.jump(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [2, 3, 0, 4, 1, 1, 1]
output = 3
if solution.jump(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [3, 2, 1]
output = 1
if solution.jump(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [2, 3, 1]
output = 1
if solution.jump(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [10,9,8,7,6,5,4,3,2,1,1,0]
output = 2
if solution.jump(nums) == output:
    print('Success')
else:
    print('Fail')
