# https://leetcode.com/problemset/all/

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        p1, p2, cur = 0, 0, 0
        result = []
        while True:
            if p1 == len1:
                result.append(nums2[p2])
                p2 += 1
            elif p2 == len2:
                result.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1
            cur += 1
            if cur == (len1 + len2) // 2 + 1:
                if (len1 + len2) % 2 == 0:
                    return (result[-2] + result[-1]) / 2
                else:
                    return float(result[-1])

nums1 = [1, 3]
nums2 = [2]
output = 2.0
solution = Solution()
if solution.findMedianSortedArrays(nums1, nums2) == output:
    print('Success')
else:
    print('Fail')

nums1 = [1, 2]
nums2 = [3, 4]
output = 2.5
solution = Solution()
if solution.findMedianSortedArrays(nums1, nums2) == output:
    print('Success')
else:
    print('Fail')


# 그냥 sorting 사용 - 시간 똑같음.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = sorted(nums1 + nums2)
        length = len(total)
        if length % 2 == 0:
            return (total[length//2 - 1] + total[length//2])/2
        else:
            return float(total[length//2])

nums1 = [1, 3]
nums2 = [2]
output = 2.0
solution = Solution()
if solution.findMedianSortedArrays(nums1, nums2) == output:
    print('Success')
else:
    print('Fail')

nums1 = [1, 2]
nums2 = [3, 4]
output = 2.5
solution = Solution()
if solution.findMedianSortedArrays(nums1, nums2) == output:
    print('Success')
else:
    print('Fail')