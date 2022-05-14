# https://programmers.co.kr/learn/courses/30/lessons/42586


# 맨 앞 인덱스에 위치한 것이 100까지 얼마나 걸리는지 확인
# 전체 프로그레스에 대해 speed * 날짜 
# 100이 넘는것들 빼냄
# 다음으로 진행
# O(n^2)
import math
def solution(progresses, speeds):
    answer = []
    while progresses:
        release = 0
        rest = math.ceil((100 - progresses[0]) / speeds[0])
        for idx in range(len(progresses)):
            progresses[idx] = progresses[idx] + rest * speeds[idx]
        
        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                release += 1
            else:
                break
        answer.append(release)
    return answer

if solution([93, 30, 55], [1, 30, 5]) == [2, 1]:
    print('Success')
else:
    print('Fail')

if solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]:
    print('Success')
else:
    print('Fail')


# O(n)
import math
def solution(progresses, speeds):
    answer = []
    days = 0
    release = 0
    for progress, speed in zip(progresses, speeds):
        if not days:
            days = math.ceil((100 - progress) / speed)
            release += 1
        else:
            val = progress + speed * days
            if  val >= 100:
                release += 1
            else:
                answer.append(release)
                days += math.ceil((100 - val)/ speed)
                release = 1
    if release:
        answer.append(release)
    return answer

if solution([93, 30, 55], [1, 30, 5]) == [2, 1]:
    print('Success')
else:
    print('Fail')

if solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]:
    print('Success')
else:
    print('Fail')

# O(n) - ver2
import math
def solution(progresses, speeds):
    answer = []
    days = math.ceil((100 - progresses[0]) / speeds[0])
    release = 1
    for idx in range(1, len(progresses)):
        progress = progresses[idx]
        speed = speeds[idx]
        val = progress + speed * days
        if val >= 100:
            release += 1
        else:
            days += math.ceil((100 - val)/ speed)
            answer.append(release)
            release = 1
    answer.append(release)
    return answer

if solution([93, 30, 55], [1, 30, 5]) == [2, 1]:
    print('Success')
else:
    print('Fail')

if solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]:
    print('Success')
else:
    print('Fail')