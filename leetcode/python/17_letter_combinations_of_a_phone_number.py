# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        candidate = []
        for digit in digits:
            if not candidate:
                candidate = digit_map[digit]
            else:
                product_list = list(itertools.product(candidate, digit_map[digit]))
                candidate = list(map(lambda x: ''.join(x), product_list))
        return candidate
        


        

solution = Solution()
digits = "23"
output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
if solution.letterCombinations(digits) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
digits = "2"
output = ["a", "b", "c"]
if solution.letterCombinations(digits) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
digits = "234"
output = ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
if solution.letterCombinations(digits) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
digits = ""
output = []
if solution.letterCombinations(digits) == output:
    print('Success')
else:
    print('Fail')