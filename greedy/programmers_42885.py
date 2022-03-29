# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    # 구명보트 최대 2명
    # 가장 적게 활용하여 모든 사람 구출
    people = sorted(people)
    start, end = 0, len(people)-1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1

    return answer

people = [70, 50, 80, 50]
limit = 100
result = 3
if solution(people, limit) == result:
    print('Success')
else:
    print('Fail')

people = [70, 80, 50]
limit = 100
result = 3
if solution(people, limit) == result:
    print('Success')
else:
    print('Fail')

people = [40, 40, 60, 60]
limit = 100
result = 2
if solution(people, limit) == result:
    print('Success')
else:
    print('Fail')