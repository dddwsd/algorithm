# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def romanToInt(self, s: str) -> int:
        value_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        answer = 0
        cur = 0
        length = len(s)
        while cur < length:
            if s[cur:cur+2] in value_dict:
                answer += value_dict[s[cur:cur+2]]
                cur += 2
            elif s[cur] in value_dict:
                answer += value_dict[s[cur]]
                cur += 1
        return answer


solution = Solution()
num = 'III'
output = 3
if solution.romanToInt(num) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
num = 'LVIII'
output = 58
if solution.romanToInt(num) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
num = 'MCMXCIV'
output = 1994
if solution.romanToInt(num) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
num = 'LX'
output = 60
if solution.romanToInt(num) == output:
    print('Success')
else:
    print('Fail')