# https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    answer = True

    dic = {}
    for item in phone_book:
        length = len(item)
        if length not in dic:
            dic[length] = {}
        if item in dic[length]:
            return False
        dic[length][item] = 0

    for key in dic:
        for item in phone_book:
            length = len(item)
            if length > key:
                pre = item[:key]
                if pre in dic[key]:
                    return False
    return answer

phone_book = ["119", "97674223", "1195524421"]
result = False
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')

phone_book = ["123","456","789"]
result = True
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')

phone_book = ["123","123","789"]
result = False
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')

phone_book = ["12","123","1235","567","88"]
result = False
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')


phone_book = ["119", "114", "112", "123223123", "1231231234"]
result = True
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')

# 좋은 다른 사람의 풀이.
# 어차피 접두사가 될 경우만 만족하기에 sort하면 앞뒤로 위치하게 된다.
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book = ["119", "97674223", "1195524421"]
result = False
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')

phone_book = ["123","456","789"]
result = True
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')

phone_book = ["123","123","789"]
result = False
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')

phone_book = ["12","123","1235","567","88"]
result = False
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')


phone_book = ["119", "114", "112", "123223123", "1231231234"]
result = True
if solution(phone_book) == result:
    print('Success')
else:
    print('Fail')
