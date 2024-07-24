from typing import List

"""
Runtime
1108ms / 55.43%
Memory
26.72MB / 16.85%
"""
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_dict = {}
        for num in nums:
            mapped_value = ""
            for str_num in str(num):
                mapped_value += str(mapping[int(str_num)])
            mapped_value = int(mapped_value)
            if mapped_value not in mapped_dict:
                mapped_dict[mapped_value] = []
            mapped_dict[mapped_value].append(num)
        result = []
        for mapped_value in sorted(mapped_dict):
            result.extend(mapped_dict[mapped_value])
        return result


"""
Runtime
761ms / 98.37%
Memory
22.49MB / 90.22%
"""
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_function(num):
            if num == 0: return mapping[0]
            res = 0
            curr = 1
            while num:
                res += mapping[num%10]*curr
                num //= 10
                curr *= 10
            return res
        # list.sort() preserves the relative order of elements
        nums.sort(key = lambda x: mapped_function(x))
        return nums

solution = Solution()
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
output = [338,38,991]
if solution.sortJumbled(mapping, nums) == output:
    print('Success')
else:
    print('Fail')
