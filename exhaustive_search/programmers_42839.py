# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
def solution(numbers):
    answer = []
    numbers = list(numbers)
    results = []
    for idx in range(len(numbers)):
        results.extend(list(set(list(permutations(numbers,idx+1)))))
    def is_prime(num):
        if num in [0, 1]:
            return False
        for idx in range(2, num//2 + 1):
            if num % idx == 0:
                return False
        return True
    for item in results:
        val = int(''.join(item))
        if is_prime(val):
            answer.append(val)
    return len(set(answer))

numbers = "17"
result = 3
if solution(numbers) == result:
    print('Suceess')
else:
    print('Fail')

numbers = "011"
result = 2
if solution(numbers) == result:
    print('Suceess')
else:
    print('Fail')