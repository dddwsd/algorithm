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

"""
Two pointer except first element - skip duplicate
Runtime
543ms / 40.89%
Memory
16.59MB / 61.39%
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        for a_idx in range(length-3):
            if a_idx > 0 and nums[a_idx] == nums[a_idx-1]:
                continue
            a = nums[a_idx]
            for b_idx in range(a_idx+1, length-2):
                if b_idx > a_idx+1 and nums[b_idx] == nums[b_idx-1]:
                    continue
                b = nums[b_idx]
                left = b_idx+1
                right = length - 1
                while left < right:
                    c = nums[left]
                    d = nums[right]
                    if a+b+c+d == target:
                        result.append([a,b,c,d])
                        left += 1
                        right -= 1
                        while nums[left-1] == nums[left]:
                            left += 1
                            if left >= right:
                                break
                        while nums[right] == nums[right+1]:
                            right -=1
                            if left >= right:
                                break
                    elif a+b+c+d < target:
                        left += 1
                    else:
                        right -= 1
        return result

"""
kSum algorithm
Runtime
64ms / 95.91%
Memory
16.70MB / 25.62%
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums, start, target, k):
            res = []
            if start >= len(nums):
                return res
            if target < nums[start]*k or target > nums[-1]*k:
                return res
            if k == 2:
                return twoSum(nums, start, target)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                for subset in kSum(nums, i + 1, target - nums[i], k - 1):
                    res.append([nums[i]] + subset)
            return res

        def twoSum(nums, start, target):
            ans = []
            i, j = start, len(nums) - 1
            while i < j:
                total = nums[i] + nums[j]
                if total < target or (i > start and nums[i] == nums[i - 1]):
                    i += 1
                elif total > target or (j < len(nums) - 1 and nums[j] == nums[j + 1]):
                    j -= 1
                else:
                    ans.append([nums[i], nums[j]])
                    i += 1
                    j -= 1
            return ans

        nums.sort()
        return kSum(nums, 0, target, 4)



solution = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
if solution.fourSum(nums, target) == output:
    print('Success')
else:
    print('Fail')


solution = Solution()
nums = [-2,-1,-1,1,1,2,2]
target = 0
output = [[-2,-1,1,2],[-1,-1,1,1]]
if solution.fourSum(nums, target) == output:
    print('Success')
else:
    print('Fail')
