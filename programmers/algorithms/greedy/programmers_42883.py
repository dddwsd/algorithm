# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    st = []
    # 모든 숫자를 확인
    for item in number:
        # k != 0인 경우 현재의 값보다 작은 값이 st에 있다면 빼내고 넣기
        while st and k > 0 and st[-1] < item:
            st.pop()
            k -= 1
        st.append(item)
    # k=0을 만들지 못한경우 내림차순으로 정렬되어있기에 앞에 len(st)-k만큼만 return하면 된다.
    return ''.join(st[:len(st) - k])

number = '1924'
k = 2
result = '94'
if solution(number, k) == result:
    print('Success')
else:
    print('Fail')

number = '1231234'
k = 3
result = '3234'
if solution(number, k) == result:
    print('Success')
else:
    print('Fail')

number = '4177252841'
k = 4
result = '775841'
if solution(number, k) == result:
    print('Success')
else:
    print('Fail')

number = '121111'
k = 1
result = '21111'
if solution(number, k) == result:
    print('Success')
else:
    print('Fail')


number = '91119'
k = 2
result = '919'
if solution(number, k) == result:
    print('Success')
else:
    print('Fail')

number = '4321'
k = 2
result = '43'
if solution(number, k) == result:
    print('Success')
else:
    print('Fail')
