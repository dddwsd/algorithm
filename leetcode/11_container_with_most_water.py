# https://leetcode.com/problems/container-with-most-water/

# 890ms
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start = 0
        end = len(height)-1

        while start < end:
            answer = max(answer, (end-start) * min(height[start], height[end]))
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
        return answer

# Improve above solution through skip small height.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start = 0
        end = len(height)-1

        while start < end:
            answer = max(answer, (end-start) * min(height[start], height[end]))
            if height[start] >= height[end]:
                cur_height = height[end]
                end -= 1
                while height[end] <= cur_height and start < end:
                    end -= 1
            else:
                cur_height = height[start]
                start += 1
                while height[start] <= cur_height and start < end:
                    start += 1

        return answer


solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
output = 49
if solution.maxArea(height) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
height = [1, 1]
output = 1
if solution.maxArea(height) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
height = [1, 2, 4, 3]
output = 4
if solution.maxArea(height) == output:
    print('Success')
else:
    print('Fail')