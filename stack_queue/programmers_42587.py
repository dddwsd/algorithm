# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 1
    locations = [i for i in range(len(priorities))]
    while priorities:
        first = max(priorities)
        idx = priorities.index(first)
        loc = locations[idx]
        if loc == location:
            return answer
        else:
            if idx == len(priorities) - 1:
                priorities = priorities[:idx]
                locations = locations[:idx]
            elif idx == 0:
                priorities = priorities[1:]
                locations = locations[1:]
            else:
                priorities = priorities[idx+1:] + priorities[:idx]
                locations = locations[idx+1:] + locations[:idx]        
        answer += 1


if solution([2, 1, 3, 2], 2) == 1:
    print('Success')
else:
    print('Fail')

if solution([1, 1, 9, 1, 1, 1], 0) == 5:
    print('Success')
else:
    print('Fail')

if solution([9, 1, 1, 1], 2) == 3:
    print('Success')
else:
    print('Fail')

if solution([1, 1, 1, 9], 2) == 4:
    print('Success')
else:
    print('Fail')