from typing import List

"""
Runtime
321ms / 61.35%
Memory
22.63MB / 9.88%
"""
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        transpose = list(zip(*score))
        transpose[k] = sorted(transpose[k], reverse=True)
        result = [0] * len(score)
        for item in score:
            idx = transpose[k].index(item[k])
            result[idx] = item
        return result

"""
Runtime
323ms / 52.55%
Memory
22.64MB / 9.88%
"""
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)

solution = Solution()
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
output = [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
if solution.sortTheStudents(score, k) == output:
    print('Success')
else:
    print('Fail')
