# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1])
    camera = []
    for start, end in routes:
        if not camera:
            camera = [start, end]
            answer += 1
        else:
            if start > camera[1]:
                camera = [start,end]
                answer += 1
            if start > camera[0]:
                camera[0] = start
            if end < camera[1]:
                camera[1] = end

    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
result = 2

if solution(routes) == result:
    print('Success')
else:
    print('Fail')

# 이상적인 다른사람 풀이 - 위 코드를 최적화시킨 버전.
def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1])
    camera = -30001
    for start, end in routes:
        if start > camera:
            answer += 1
            camera = end

    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
result = 2

if solution(routes) == result:
    print('Success')
else:
    print('Fail')