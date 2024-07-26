from typing import List

"""
Runtime
501ms / 98.01%
Memory
23.58MB / 96.52%
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums

"""
time limit
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums

"""
merge sort
Runtime
1321ms / 16.99%
Memory
24.11MB / 62.25%
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 1:
            return nums
        mid = length//2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        left_idx = 0
        right_idx = 0
        idx = 0
        while left_idx < len(left) and right_idx < len(right):
            if left_idx == len(left):
                nums[idx] = right[right_idx]
                right_idx += 1
            elif right_idx == len(right):
                nums[idx] = left[left_idx]
                left_idx += 1
            elif left[left_idx] < right[right_idx]:
                nums[idx] = left[left_idx]
                left_idx += 1
            else:
                nums[idx] = right[right_idx]
                right_idx += 1
            idx += 1
        return nums


solution = Solution()
nums = [5,2,3,1]
outputs =[1,2,3,5]
if solution.sortArray(nums) == outputs:
    print("Success")
else:
    print("Fail")

solution = Solution()
nums = [5,1,1,2,0,0]
outputs =[0,0,1,1,2,5]
if solution.sortArray(nums) == outputs:
    print("Success")
else:
    print("Fail")
