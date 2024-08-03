from typing import List

"""
Runtinme
340ms / Beats 65.06%

Memory
33.25MB / Beats. 81.08%
"""
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        number_dict = dict()
        unique_nums = 0
        for item in arr:
            if item not in number_dict:
                number_dict[item] = 1
                unique_nums += 1
            else:
                number_dict[item] += 1

        for value in sorted(number_dict.values()):
            k -= value
            unique_nums -= 1
            if k == 0 :
                return unique_nums
            elif k < 0 :
                return unique_nums + 1


solution = Solution()
arr = [4,3,1,1,3,3,2]
k = 3
output = 2
if solution.findLeastNumOfUniqueInts(arr, k) == output:
    print('Success')
else:
    print('Fail')


solution = Solution()
arr = [5,5,4]
k = 1
output = 1
if solution.findLeastNumOfUniqueInts(arr, k) == output:
    print('Success')
else:
    print('Fail')
