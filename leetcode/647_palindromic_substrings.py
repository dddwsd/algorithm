# https://leetcode.com/problems/palindromic-substrings/

# 8772ms
class Solution:
    def sliding_window(self, s, idx, width):
        start = idx
        end = idx+width-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def countSubstrings(self, s: str) -> int:
        answer = 0
        length = len(s)
        answer += length
        for width in range(2, length+1):
            for idx in range(length-width+1):
                if self.sliding_window(s, idx, width):
                    answer += 1
        return answer

# two pointer
class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        length = len(s)
        start = 0
        while start < length:
            left = start - 1
            right = start + 1
            # 우측으로 동일글씨가 몇번 있는지.
            while right < length:
                if s[right] == s[start]:
                    right += 1
                else:
                    break
            # start부터 right - 1까지 동일한 char이다.
            cnt = right - start
            answer += cnt*(cnt+1)//2
            start = right

            # 이제 좌우로 가면서 동일한 거 찾기.
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    answer += 1
                    left -= 1
                    right += 1
                else:
                    break
        return answer
        

solution = Solution()
s = 'abc'
output = 3
if solution.countSubstrings(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = 'aaa'
output = 6
if solution.countSubstrings(s) == output:
    print('Success')
else:
    print('Fail')

solution = Solution()
s = 'aba'
output = 4
if solution.countSubstrings(s) == output:
    print('Success')
else:
    print('Fail')
