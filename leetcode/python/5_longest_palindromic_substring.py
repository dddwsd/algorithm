# https://leetcode.com/problems/longest-palindromic-substring/

# 해결방법
# string의 각 문자를 기준으로 substring이 생성되는 최대값을 구함.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        start, sub_len = 0,1
        for idx in range(length):
            if (length - idx) * 2 < sub_len:
                break
            front, back = idx, idx
            # 동일 문자가 계속 나오면 back을 뒤로 넘기기.
            while back+1 < length and s[back] == s[back+1]:
                back += 1

            # 이제 다음 문자는 front와 다른게 확실하니까
            while front > 0 and back+1 < length and s[front-1] == s[back+1]:
                front -= 1
                back += 1

            if sub_len < back + 1 - front:
                start = front
                sub_len = back + 1 - front

        return s[start:start + sub_len]

s = 'babad'
output = 'bab'
solution = Solution()
if solution.longestPalindrome(s) == output:
    print('Success')
else:
    print('Fail')

s = 'cbbd'
output = 'bb'
solution = Solution()
if solution.longestPalindrome(s) == output:
    print('Success')
else:
    print('Fail')

s = 'c'
output = 'c'
solution = Solution()
if solution.longestPalindrome(s) == output:
    print('Success')
else:
    print('Fail')

# for -> while로 변경함으로써 시간단축
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        start, sub_len, idx = 0,1,0
        while idx < length:
            if (length - idx) * 2 < sub_len:
                break
            front, back = idx, idx
            # 동일 문자가 계속 나오면 back을 뒤로 넘기기.
            while back+1 < length and s[back] == s[back+1]:
                back += 1
            idx = back

            # 이제 다음 문자는 front와 다른게 확실하니까
            while front > 0 and back+1 < length and s[front-1] == s[back+1]:
                front -= 1
                back += 1

            if sub_len < back + 1 - front:
                start = front
                sub_len = back + 1 - front
            idx += 1

        return s[start:start + sub_len]

s = 'babad'
output = 'bab'
solution = Solution()
if solution.longestPalindrome(s) == output:
    print('Success')
else:
    print('Fail')

s = 'cbbd'
output = 'bb'
solution = Solution()
if solution.longestPalindrome(s) == output:
    print('Success')
else:
    print('Fail')

s = 'c'
output = 'c'
solution = Solution()
if solution.longestPalindrome(s) == output:
    print('Success')
else:
    print('Fail')