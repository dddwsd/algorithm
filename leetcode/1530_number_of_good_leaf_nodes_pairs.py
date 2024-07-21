# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, depth=None):
        self.val = val
        self.left = left
        self.right = right

# TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: TreeNode{val: 4, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: None}}

"""
Runtime
3187ms / Beats 5.03%
Memory
17.08 MB / 42.02%
"""
import math
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        depth = 0
        idx = 0
        leafs = []
        def explore(leafs, root, idx, depth):
            if not root.left and not root.right:
                leafs.append(idx+1)
            if root.left:
                explore(leafs, root.left, 2*idx+1, depth+1)
            if root.right:
                explore(leafs, root.right, 2*idx+2, depth+1)

        explore(leafs, root, idx, depth)
        length = len(leafs)
        result = 0
        for start_idx in range(length-1):
            for end_idx in range(start_idx+1, length):
                start, end = leafs[start_idx], leafs[end_idx]
                dist = 0
                while math.log2(start) != math.log2(end):
                    if start > end:
                        start = start //2
                        dist += 1
                    if end > start:
                        end = end // 2
                        dist += 1

                while start != end:
                    if start//2 >= 1:
                        start = start //2
                        dist += 1
                    if end //2 >= 1:
                        end = end // 2
                        dist += 1
                if dist <= distance:
                    result += 1
        return result

"""
Runtime
1174ms / 15.80%
Memory
17.05MB / 42.02%
"""
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        depth = 0
        idx = 0
        leafs = []
        def explore(leafs, root, idx, depth):
            if not root.left and not root.right:
                leafs.append([idx+1, depth])
            if root.left:
                explore(leafs, root.left, 2*idx+1, depth+1)
            if root.right:
                explore(leafs, root.right, 2*idx+2, depth+1)

        explore(leafs, root, idx, depth)
        length = len(leafs)
        result = 0
        for start_idx in range(length-1):
            for end_idx in range(start_idx+1, length):
                start, start_depth = leafs[start_idx]
                end, end_depth = leafs[end_idx]
                dist = 0
                while True:
                    if start_depth != end_depth:
                        if start > end:
                            start = start //2
                            start_depth -= 1
                            dist += 1
                        if end > start:
                            end = end // 2
                            end_depth -= 1
                            dist += 1
                    elif start != end:
                        if start//2 >= 1:
                            start = start //2
                            dist += 1
                        if end //2 >= 1:
                            end = end // 2
                            dist += 1
                    else:
                        if dist <= distance:
                            result += 1
                        break
                    if dist > distance:
                        break
        return result

"""
Runtime
127ms / Beats 58.25%
Memory
16.81MB / 94.41%

depth마다 left의 leaf와 right leaf 사이의 길이 계산
"""
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def explore(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [1]

            left = explore(root.left)
            right = explore(root.right)

            for left_leaf in left:
                for right_leaf in right:
                    if left_leaf + right_leaf <= distance:
                        self.result += 1

            for idx in range(len(left)):
                left[idx] += 1
            for idx in range(len(right)):
                right[idx] += 1
            return left + right
        explore(root)
        return self.result

"""
Runtime
66ms / 98.29%
Memory
16.95MB / 68.02%

동일 distance 한번에 계산
"""
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def explore(root):
            if not root:
                return {}
            if not root.left and not root.right:
                return {1:1}

            left = explore(root.left)
            right = explore(root.right)

            for left_leaf in left:
                for right_leaf in right:
                    if left_leaf + right_leaf <= distance:
                        self.result += left[left_leaf] * right[right_leaf]

            new_dict = {}
            for left_leaf in left:
                if left_leaf < distance:
                    new_dict[left_leaf+1] = left[left_leaf]
            for right_leaf in right:
                if right_leaf < distance:
                    if right_leaf+1 not in new_dict:
                        new_dict[right_leaf+1] = 0
                    new_dict[right_leaf+1] += right[right_leaf]
            return new_dict
        explore(root)
        return self.result



solution = Solution()
root = [1,2,3,None,4]
distance = 3
output = 1
if solution.countPairs(root, distance) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
root = [7,1,4,6,None,5,3,None,None,None,None,None,2]
distance = 3
output = 1
if solution.countPairs(root, distance) == output:
    print('Success')
else:
    print('Fail')
