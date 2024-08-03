# https://leetcode.com/problems/coin-change/

# 2000ms - dp solution
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer = [2**31 -1] * (amount+1)
        answer[0] = 0
        for coin in sorted(coins, reverse=True):
            for idx in range(coin, amount+1):
                answer[idx] = min(answer[idx], answer[idx-coin]+1)

        if answer[amount] == 2**31 -1:
            return -1
        return answer[amount]


solution = Solution()
coins = [1, 2, 5]
amount = 11
output = 3
if solution.coinChange(coins, amount) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
coins = [2]
amount = 3
output = -1
if solution.coinChange(coins, amount) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
coins = [1]
amount = 0
output = 0
if solution.coinChange(coins, amount) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
coins = [186, 419, 83, 408]
amount = 6249
output = 20
if solution.coinChange(coins, amount) == output:
    print('Success')
else:
    print('Fail')