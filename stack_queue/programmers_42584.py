# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0 for _ in prices]

    length = len(answer)
    for start in range(length-1):
        for idx in range(start+1,length):
            answer[start] += 1
            if prices[start] > prices[idx]:
                break
    return answer

if solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]:
    print('Success')
else:
    print('Fail')

if solution([6, 5, 5, 2, 3]) == [1, 2, 1, 1, 0]:
    print('Success')
else:
    print('Fail')

if solution([2, 3, 3, 7, 7, 4, 1, 5]) == [6, 5, 4, 2, 1,1,1, 0]:
    print('Success')
else:
    print('Fail')

if solution([5, 8, 6, 2, 4, 1]) == [3, 1, 1, 2, 1, 0]:
    print('Success')
else:
    print('Fail')
