# https://app.codility.com/programmers/trainings/1/longest_password/start/

# (a-z, A-Z, 0-9)
# 짝수의 letters
# 홀수의 digits
import re
def solution(S):
    answer = -1
    for words in S.split():
        no_valid = re.compile('[^a-zA-Z0-9]')
        if no_valid.findall(words):
            continue

        letter_pattern = re.compile('[a-zA-Z]')
        letters = letter_pattern.findall(words)
        
        digit_pattern = re.compile('[0-9]')
        digits = digit_pattern.findall(words)
        
        if len(letters) % 2 == 0 and len(digits) % 2 == 1:
            answer = max(answer, len(words))
    return answer



S = 'test 5 a0A pass007 ?xy1'
result = 7
if solution(S) == result:
    print('Success')
else:
    print('Fail')

S = 'pass007'
result = 7
if solution(S) == result:
    print('Success')
else:
    print('Fail')

S = '?xy1'
result = -1
if solution(S) == result:
    print('Success')
else:
    print('Fail')