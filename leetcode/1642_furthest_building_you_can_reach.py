from typing import List
from collections import deque

"""
Memory Limit Exceeded
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        cases = deque([[bricks, ladders]])
        for idx in range(1, len(heights)):
            diff = heights[idx] - heights[idx-1]
            if diff <= 0:
                continue

            length = len(cases)
            while length:
                length -= 1
                bricks, ladders = cases.popleft()
                if ladders:
                    cases.append([bricks, ladders - 1])
                if bricks >= diff:
                    cases.append([bricks - diff, ladders])

            if not cases:
                return idx - 1

        return idx

"""
Time Limit
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        length = len(heights)
        def next_step(heights, idx, bricks, ladders):
            if length <= idx:
                return idx - 1
            diff = heights[idx] - heights[idx-1]
            value = 0
            if diff <= 0:
                value = max(value, next_step(heights, idx+1, bricks, ladders))
            else:
                if ladders:
                    value = max(value, next_step(heights, idx+1, bricks, ladders-1))
                if bricks >= diff:
                    value = max(value, next_step(heights, idx+1, bricks-diff, ladders))
            return max(value, idx-1)
        return next_step(heights, 1, bricks, ladders)

"""
Runtime
864ms / Beats 5.00%

Memory
31.04MB / 28.46%
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        binary search를 통해 해당 idx에 해당하는 heights까지 갈 수 있는지 확인.
        """
        def canReach(mid):
            required_bricks = []
            for i in range(mid):
                diff = heights[i + 1] - heights[i]
                if diff > 0:
                    required_bricks.append(diff)

            required_bricks.sort(reverse=True)
            total_bricks = sum(required_bricks[ladders:])

            return total_bricks <= bricks

        low, high = 0, len(heights) - 1

        while low < high:
            mid = (low + high + 1) // 2
            if canReach(mid):
                low = mid
            else:
                high = mid - 1

        return low

"""
Runtime
424ms / Beats 50.70%

Memory
31.06MB / 28.46%
"""
import heapq # min heap 자료구조 제공
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for idx in range(1, len(heights)):
            diff = heights[idx] - heights[idx-1]
            if diff <= 0:
                continue

            heapq.heappush(heap, diff)
            if ladders:
                ladders -= 1
            else:
                bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return idx -1
        return idx




solution = Solution()
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
output = 4
if solution.furthestBuilding(heights, bricks, ladders) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
heights = [14, 3, 19, 3]
bricks = 17
ladders = 0
output = 3
if solution.furthestBuilding(heights, bricks, ladders) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
heights = [1,5,1,2,3,4,10000]
bricks = 4
ladders = 1
output = 5
if solution.furthestBuilding(heights, bricks, ladders) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
output = 7
if solution.furthestBuilding(heights, bricks, ladders) == output:
    print('Success')
else:
    print('Fail')
