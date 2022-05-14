# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    # money[n] = max(money[n-1], money[n] + money[n-2])
    if len(money) <= 3:
        return max(money)

    money_v2 = []
    for val in money:
        money_v2.append(val)
    money_v2[2] = max(money_v2[1], money_v2[2])
    money[1] = max(money[0], money[1])

    length = len(money)
    # 첫번쨰 포함 마지막 미포함
    for idx in range(2, length-1):
        money[idx] = max(money[idx-1], money[idx] + money[idx-2])
    # 첫번쨰 미포함 마지막 포함
    for idx in range(3, length):
        money_v2[idx] = max(money_v2[idx-1], money_v2[idx] + money_v2[idx-2])
    return max(money[-2], money_v2[-1])

money = [1, 2, 3, 4]
result = 6
if solution(money) == result:
    print('Success')
else:
    print('Fail')

money = [90,0,0,95,1,1]
result = 185
if solution(money) == result:
    print('Success')
else:
    print('Fail')

# 위 풀이를 list말고 변수로만 체크
def solution(money):
    # money[n] = max(money[n-1], money[n] + money[n-2])
    if len(money) <= 3:
        return max(money)

    with_x0, with_x1 = money[0], max(money[0], money[1])
    wout_x0, wout_x1 = money[1], max(money[1], money[2])

    length = len(money)
    # 첫번쨰 포함 마지막 미포함
    for idx in range(2, length-1):
        temp = with_x1
        with_x1 = max(with_x1, money[idx] + with_x0)
        with_x0 = temp

        temp = wout_x1
        wout_x1 = max(wout_x1, money[idx+1] + wout_x0)
        wout_x0 = temp
    return max(with_x0, with_x1, wout_x0, wout_x1)

money = [1, 2, 3, 4]
result = 6
if solution(money) == result:
    print('Success')
else:
    print('Fail')

money = [90,0,0,95,1,1]
result = 185
if solution(money) == result:
    print('Success')
else:
    print('Fail')
