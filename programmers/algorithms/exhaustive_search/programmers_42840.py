# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    result = [0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for idx in range(len(answers)):
        if answers[idx] == first[idx%5]:
            result[0] += 1
        if answers[idx] == second[idx%8]:
            result[1] += 1
        if answers[idx] == third[idx%10]:
            result[2] += 1    
    max_answer = max(result)
    for idx, item in enumerate(result):
        if item == max_answer:
            answer.append(idx+1)
    return answer


answers = [1, 2, 3, 4, 5]
result = [1]
if solution(answers) == result:
    print('Success')
else:
    print('Fail')

answers = [1, 3, 2, 4, 2]
result = [1, 2, 3]
if solution(answers) == result:
    print('Success')
else:
    print('Fail')
