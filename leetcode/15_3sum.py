# https://leetcode.com/problems/3sum/

from typing import List

# brute force - time limit
import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        candidates = collections.deque()
        val_num = collections.defaultdict(int)
        dup_check = set()
        for val in sorted(nums):
            if val != 0 and val_num[val] == 2:
                continue
            elif val == 0 and val_num[val] == 3:
                continue
            val_num[val] += 1

            length = len(candidates)
            for idx in range(length):
                exist = candidates[idx]
                exist_string = '|'.join(map(str, exist + [val]))
                if exist_string in dup_check:
                    continue
                dup_check.add(exist_string)
                if len(exist) < 2:
                    candidates.append(exist + [val])
                elif sum(exist) + val == 0:
                    answer.append(exist + [val])
            candidates.append([val])

        return sorted(answer, key=lambda x: (x[0], x[1], x[2]))

# two pointer - 4000ms

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        length = len(nums)-1
        val_check = set()
        for idx in range(1, length):
            left = idx - 1
            right = idx + 1
            while left > -1 and right < length + 1:
                add_val = nums[left] + nums[idx] + nums[right]
                if add_val == 0:
                    val_string = '|'.join(map(str,[nums[left], nums[idx], nums[right]]))
                    if val_string not in val_check:
                        answer.append([nums[left], nums[idx], nums[right]])
                        val_check.add(val_string)
                    left -= 1
                    right += 1
                    while left > -1 and nums[left] == nums[left+1]:
                        left -= 1
                    while right < length + 1 and nums[right-1] == nums[right]:
                        right += 1
                else:
                    if add_val > 0 :
                        left -= 1
                    else:
                        right += 1

        return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


# two pointer - 4000ms

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        length = len(nums)
        for idx in range(length - 2):
            if idx and nums[idx-1] == nums[idx]:
                continue
            left = idx + 1
            right = length - 1
            while right < length and left < right:
                add_val = nums[idx] + nums[left] + nums[right]
                if add_val == 0:
                    answer.append([nums[idx], nums[left], nums[right]])
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                else:
                    if add_val < 0 :
                        left += 1
                    else:
                        right -= 1

        return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
output = [[-1, -1, 2], [-1, 0, 1]]
if solution.threeSum(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = []
output = []
if solution.threeSum(nums) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
nums = [0, 0, 0, 0]
output = [[0, 0, 0]]
if solution.threeSum(nums) == output:
    print('Success')
else:
    print('Fail')
