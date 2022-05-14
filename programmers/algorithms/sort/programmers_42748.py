# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for item in commands:
        i,j,k = item
        i -= 1
        j -= 1
        k -= 1
        answer.append(sorted(array[i:j+1])[k])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
result = [5, 6, 3]
if solution(array, commands) == result:
    print('Success')
else:
    print('Fail')

# Using merge sort
def solution(array, commands):
    answer = []
    def merge_sort(arr):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        low_arr = merge_sort(arr[:mid])
        high_arr = merge_sort(arr[mid:])

        merged_arr = []
        l = h = 0
        while l < len(low_arr) and h < len(high_arr):
            if low_arr[l] < high_arr[h]:
                merged_arr.append(low_arr[l])
                l += 1
            else:
                merged_arr.append(high_arr[h])
                h += 1
        merged_arr += low_arr[l:]
        merged_arr += high_arr[h:]
        return merged_arr

    for item in commands:
        i,j,k = item
        i -= 1
        j -= 1
        k -= 1
        answer.append(merge_sort(array[i:j+1])[k])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
result = [5, 6, 3]
if solution(array, commands) == result:
    print('Success')
else:
    print('Fail')
