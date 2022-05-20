# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        value_dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM',
        }

        answer = ''
        for point in range(3, -1, -1):
            share_num = num // (10**point) * (10**point)
            num -= share_num
            if share_num in value_dict:
                answer += value_dict[share_num]
            else:
                if share_num >= 5 * (10 ** point):
                    answer += value_dict[5 * (10 ** point)]
                    share_num -= 5 * (10 ** point)
                multiple_count = share_num // (10 ** point) 
                answer += multiple_count * value_dict[10 ** point]
                
        return answer


solution = Solution()
num = 3
output = 'III'
if solution.intToRoman(num) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
num = 58
output = 'LVIII'
if solution.intToRoman(num) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
num = 1994
output = 'MCMXCIV'
if solution.intToRoman(num) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
num = 60
output = 'LX'
if solution.intToRoman(num) == output:
    print('Success')
else:
    print('Fail')