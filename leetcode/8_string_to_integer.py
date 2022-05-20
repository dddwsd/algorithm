# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        # iganore andy leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # check final result is negative or positive
        flag = 1
        if s[0] == '-':
            flag = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # read next characters until the next non-digit character

        value = ''
        for char in s:
            try:
                int(char)
                value += char
            except:
                break
        
        # convert digits into an integer
        if value:
            value = flag * int(value)
        else:
            value = 0
        
        # If out of range [-1*2**31, 2**31-1],
        # clamp the integer so that it remains in the range.
        if value < -1 * (2 ** 31):
            value = -1 * (2 ** 31)
        elif value > 2 ** 31 - 1:
            value = 2 ** 31 - 1
        
        return value

            

        


solution = Solution()
s = '42'
output = 42
if solution.myAtoi(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = '   -42'
output = -42
if solution.myAtoi(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = '4193 with words'
output = 4193
if solution.myAtoi(s) == output:
    print('Success')
else:
    print('Fail')

