"""
2976 - Minimum Cost to Convert STring I
Floyd-Warshall algorithm

"""
from typing import List
from collections import deque

"""
Time Limit
"""
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        change_dict = {}
        for start, end, value in zip(original, changed, cost):
            if start not in change_dict:
                change_dict[start] = {}
            if end not in change_dict[start]:
                change_dict[start][end] = 10**6+1
            change_dict[start][end] = min(change_dict[start][end], value)

        result = 0
        for start, end in zip(source, target):
            if start == end:
                continue
            if start not in change_dict:
                result = -1
                break
            if end not in change_dict[start]:
                change_dict[start][end] = 10**100
            convert_queue = deque([[start,0]])
            value = change_dict[start][end]
            while convert_queue:
                cur, nested_value = convert_queue.popleft()
                if cur not in change_dict:
                    continue
                for dest in change_dict[cur]:
                    cur_value = nested_value + change_dict[cur][dest]
                    if dest in change_dict[start] and cur_value > change_dict[start][dest]:
                        continue
                    else:
                        change_dict[start][dest] = cur_value
                    # print(start, dest, cur_value)
                    if dest == end:
                        value = min(value, cur_value)
                    else:
                        if cur_value < value:
                            convert_queue.append([dest, cur_value])
            if value < 10**100:
                result += value
            else:
                result = -1
                break
        return result

"""
Runtime
2068ms / 29.36%
Memory
18.11MB / 76.61%
"""
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        matrix = [ [float('inf')] * 26 for _ in range(26) ]
        for idx in range(26):
            matrix[idx][idx] = 0

        for start, end, value in zip(original, changed, cost):
            start_idx = ord(start) - ord('a')
            end_idx = ord(end) - ord('a')
            matrix[start_idx][end_idx] = min(matrix[start_idx][end_idx], value)

        for mid in range(26):
            for start in range(26):
                for end in range(26):
                    matrix[start][end] = min(matrix[start][end], matrix[start][mid] + matrix[mid][end])

        result = 0
        for start, end in zip(source, target):
            start_idx = ord(start) - ord('a')
            end_idx = ord(end) - ord('a')

            if matrix[start_idx][end_idx] == float('inf'):
                result = -1
                break

            result += matrix[start_idx][end_idx]
        return result

"""
Runtime
867ms / 87.62%
Memory
18.18MB / 76.61%
"""
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        matrix = {}
        for start, end, value in zip(original, changed, cost):
            if start not in matrix:
                matrix[start] = {}
            if end not in matrix[start]:
                matrix[start][end] = float('inf')
            matrix[start][start] = 0
            matrix[start][end] = min(matrix[start][end], value)

        for start in matrix.keys():
            queue = deque()
            for dest in matrix[start]:
                if dest not in matrix:
                    continue
                queue.append(dest)

            while queue:
                point = queue.popleft()
                for dest in matrix[point]:
                    value = matrix[point][dest]
                    value_from_start = matrix[start][point] + value
                    if dest not in matrix[start]:
                        matrix[start][dest] = float('inf')
                    if value_from_start >= matrix[start][dest]:
                        continue
                    matrix[start][dest] = min(matrix[start][dest], value_from_start)
                    if dest in matrix:
                        queue.append(dest)

        result = 0
        for start, end in zip(source, target):
            if start == end:
                continue
            if start not in matrix:
                return -1
            if end not in matrix[start]:
                return -1
            result += matrix[start][end]
        return result

"""
Fix Time Limit Code
Runtime
3273ms / 16.52%
Memory
18.49MB / 28.90%
"""
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        change_dict = {}
        for start, end, value in zip(original, changed, cost):
            if start not in change_dict:
                change_dict[start] = {}
            if end not in change_dict[start]:
                change_dict[start][end] = float('inf')
            change_dict[start][start] = 0
            change_dict[start][end] = min(change_dict[start][end], value)

        result = 0

        passed_point = set()
        for start, end in zip(source, target):
            if (start,end) in passed_point:
                result += change_dict[start][end]
                continue
            if start == end:
                continue
            if start not in change_dict:
                return -1

            queue = deque([])
            for dest in change_dict[start]:
                if dest not in change_dict:
                    continue
                queue.append(dest)

            while queue:
                cur = queue.popleft()
                for dest in change_dict[cur]:
                    value = change_dict[cur][dest]
                    value_from_start = change_dict[start][cur] + value
                    if dest not in change_dict[start]:
                        change_dict[start][dest] = float('inf')
                    if value_from_start >= change_dict[start][dest]:
                        continue
                    change_dict[start][dest] = min(change_dict[start][dest], value_from_start)
                    if dest not in change_dict:
                        continue
                    queue.append(dest)

            if end not in change_dict[start]:
                return -1
            result += change_dict[start][end]
            passed_point.add((start,end))
        return result



solution = Solution()
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
output = 28
if solution.minimumCost(source, target, original, changed, cost) == output:
    print('Success')
else:
    print('Fail')


solution = Solution()
source = "aaaa"
target = "bbbb"
original = ["a","c"]
changed = ["c","b"]
cost = [1,2]
output = 12
if solution.minimumCost(source, target, original, changed, cost) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
source = "abcd"
target = "abce"
original = ["a"]
changed = ["e"]
cost = [10000]
output = -1
if solution.minimumCost(source, target, original, changed, cost) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
source = "aabdbaabaa"
target = "bdaacabcab"
original = ["b","d","d","a","c","c","a","d","a","b"]
changed = ["c","c","b","d","b","d","b","a","c","a"]
cost = [9,1,7,9,2,1,3,8,8,2]
output = 43
if solution.minimumCost(source, target, original, changed, cost) == output:
    print('Success')
else:
    print('Fail')
