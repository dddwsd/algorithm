from typing import List


"""
Runtime
177ms / 80.98%
Memory
17.41MB / 12.50%
"""
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """
        Convex Hulls - Graham scan
        """
        def outer_product(point1, point2, point3):
            """
            2차원 평면에서의 외적값 = Counter Clock Wise
            양수일 경우 오른손 법칙에 의해 point3은 point1과 point2를 이은 선분의 왼쪽
            음수일 경우 오른손 법칙에 의해 point3은 point1과 point2를 이은 선분의 오른쪽
            """
            x_point1, y_point1 = point1
            x_point2, y_point2 = point2
            x_point3, y_point3 = point3
            return ((y_point3 - y_point2)*(x_point2 - x_point1)) - ((y_point2 - y_point1)*(x_point3 - x_point2))

        trees.sort()
        upper, lower = [], []
        for point in trees:
            # 상단 다각형의 경우 point가 왼쪽에 위치할 경우 빼내야 하고 오른쪽에 위치하는 것들만 찾아야 함
            while len(upper) > 1 and outer_product(upper[-2], upper[-1], point) > 0:
                upper.pop()
            # 하단 다각형의 경우 point가 오른쪽에 위치할 경우 빼내야 하고 왼쪽에 위치하는 것들만 찾아야함.
            while len(lower) > 1 and outer_product(lower[-2], lower[-1], point) < 0:
                lower.pop()
            upper.append(tuple(point))
            lower.append(tuple(point))
        return list(set(upper + lower))



solution = Solution()
trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
output = [[1,1],[2,0],[4,2],[3,3],[2,4]]
if solution.outerTrees(trees) == output:
    print('Success')
else:
    print('Fail')
