# https://programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
    if list(set(numbers)) == [0]:
        return '0'
    numbers = list(map(str, numbers))
    def merge_sort(arr):
        if len(arr) < 2:
            return arr
        
        mid = len(arr) // 2
        low_arr = merge_sort(arr[:mid])
        high_arr = merge_sort(arr[mid:])

        l = h = 0
        merged_arr = []
        while l < len(low_arr) and h < len(high_arr):
            if low_arr[l] + high_arr[h] < high_arr[h] + low_arr[l]:
                merged_arr.append(low_arr[l])
                l += 1
            else:
                merged_arr.append(high_arr[h])
                h += 1
        merged_arr += low_arr[l:]
        merged_arr += high_arr[h:]
        return merged_arr

    numbers = merge_sort(numbers)
    answer = ''.join(numbers[::-1])
    return answer


numbers = [6, 10, 2]
result = "6210"
if solution(numbers) == result:
    print('Success')
else:
    print('Fail')

numbers = [3, 30, 34, 5, 9]
result = "9534330"
if solution(numbers) == result:
    print('Success')
else:
    print('Fail')

numbers = [3]
result = "3"
if solution(numbers) == result:
    print('Success')
else:
    print('Fail')

numbers = [0, 0, 0, 0]
result = "0"
if solution(numbers) == result:
    print('Success')
else:
    print('Fail')

# 다른사람의 경이로운 풀이..
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


numbers = [6, 10, 2]
result = "6210"
if solution(numbers) == result:
    print('Success')
else:
    print('Fail')

numbers = [3, 30, 34, 5, 9]
result = "9534330"
if solution(numbers) == result:
    print('Success')
else:
    print('Fail')

numbers = [3]
result = "3"
if solution(numbers) == result:
    print('Success')
else:
    print('Fail')

numbers = [0, 0, 0, 0]
result = "0"
if solution(numbers) == result:
    print('Success')
else:
    print('Fail')