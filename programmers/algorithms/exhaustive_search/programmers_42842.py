# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    # 가로, 세로 3이상
    # 가로 >= 세로
    # 가로 * 세로 = brwon + yellow
    # 가로 * 2 + (세로-2)*2 = brown
    # (가로-2) * (세로-2) = yello
    width = 3
    while True:
        for height in range(3, width+1):
            if width * height == brown + yellow:
                if width*2 + (height-2)*2 == brown:
                    if (width-2) * (height-2) == yellow:
                        return [width, height]
        width += 1

brown = 10
yellow = 2
result = [4, 3]
if solution(brown, yellow) == result:
    print('Success')
else:
    print('Fail')

brown = 8
yellow = 1
result = [3, 3]
if solution(brown, yellow) == result:
    print('Success')
else:
    print('Fail')

brown = 24
yellow = 24
result = [8, 6]
if solution(brown, yellow) == result:
    print('Success')
else:
    print('Fail')


def solution(brown, yellow):
    # 가로, 세로 3이상
    # 가로 >= 세로
    # 가로 * 세로 = brwon + yellow
    # 가로 * 2 + (세로-2)*2 = brown
    # (가로-2) * (세로-2) = yello
    width = 3
    while True:
        for height in range(3, width+1):
            if width * height == brown + yellow:
                if width*2 + (height-2)*2 == brown:
                    if (width-2) * (height-2) == yellow:
                        return [width, height]
        width += 1

brown = 10
yellow = 2
result = [4, 3]
if solution(brown, yellow) == result:
    print('Success')
else:
    print('Fail')

brown = 8
yellow = 1
result = [3, 3]
if solution(brown, yellow) == result:
    print('Success')
else:
    print('Fail')

brown = 24
yellow = 24
result = [8, 6]
if solution(brown, yellow) == result:
    print('Success')
else:
    print('Fail')


def solution(brown, yellow):
    # 가로, 세로 3이상
    # 가로 >= 세로
    # 가로 * 세로 = brwon + yellow
    # 가로 * 2 + (세로-2)*2 = brown
    # (가로-2) * (세로-2) = yello
    width = 3
    while True:
        if (brown + yellow) % width != 0:
            width += 1
            continue
        height = (brown + yellow) / width
        if width*2 + (height-2)*2 == brown:
            if (width-2) * (height-2) == yellow:
                return sorted([width, height],reverse=True)
        width += 1

brown = 10
yellow = 2
result = [4, 3]
if solution(brown, yellow) == result:
    print('Success')
else:
    print('Fail')

brown = 8
yellow = 1
result = [3, 3]
if solution(brown, yellow) == result:
    print('Success')
else:
    print('Fail')

brown = 24
yellow = 24
result = [8, 6]
if solution(brown, yellow) == result:
    print('Success')
else:
    print('Fail')