# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
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

    citations = merge_sort(citations)
    for idx in range(len(citations)):
        if citations[idx] >= len(citations) - idx:
            return len(citations) - idx
    return 0

citations = [3, 0, 6, 1, 5]
result = 3
if solution(citations) == result:
    print('Success')
else:
    print('Fail')

# n = 6 h 4 
citations = [1, 1, 5, 5, 5, 5]
result = 4
if solution(citations) == result:
    print('Success')
else:
    print('Fail')

# n = 6 h 4 
citations = [0, 2]
result = 1
if solution(citations) == result:
    print('Success')
else:
    print('Fail')

# n = 6 h 4 
citations = [0, 0]
result = 0
if solution(citations) == result:
    print('Success')
else:
    print('Fail')
