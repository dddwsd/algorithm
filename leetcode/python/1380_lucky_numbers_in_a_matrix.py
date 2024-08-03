from typing import List

"""
Runtime
98ms / Beats 97.40%
Memory
16.84 MB / Beats 43.01%
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # luckey number: minimum for row & maximum for column
        col_length = len(matrix)
        results = []
        for row in matrix:
            small = sorted(row)[0]
            min_index = row.index(small)
            lucky_numbers = True
            for col_idx in range(col_length):
                if small < matrix[col_idx][min_index]:
                    lucky_numbers = False
                    break
            if lucky_numbers:
                results.append(small)
        return results



solution = Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
outputs =[15]
if solution.luckyNumbers(matrix) == outputs:
    print("Success")
else:
    print("Fail")

solution = Solution()
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
outputs =[12]
if solution.luckyNumbers(matrix) == outputs:
    print("Success")
else:
    print("Fail")
