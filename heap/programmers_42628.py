# https://programmers.co.kr/learn/courses/30/lessons/42628

class Heap(object):
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.length = 0
    
    def push(self, val):
        self.length += 1
        # for max heap
        self.max_heap.append(val)
        cur = self.length - 1
        while self.max_heap[cur//2] < self.max_heap[cur]:
            self.max_heap[cur//2], self.max_heap[cur] = self.max_heap[cur], self.max_heap[cur//2]
            cur //= 2
        # for min heap
        self.min_heap.append(val)
        cur = self.length - 1
        while self.min_heap[cur//2] > self.min_heap[cur]:
            self.min_heap[cur//2], self.min_heap[cur] = self.min_heap[cur], self.min_heap[cur//2]
            cur //= 2

    def pop_max(self):
        # 비어 있는 경우
        if self.length == 0:
            return 0
        # 비어 있지 않은 경우
        self.length -= 1
        if self.length == 0:
            self.min_heap.pop()
            return self.max_heap.pop()

        # for max heap
        self.max_heap[0], self.max_heap[-1] = self.max_heap[-1], self.max_heap[0]
        max_val = self.max_heap.pop()
        cur = 0
        while True:
            left_idx = (cur+1) * 2 - 1
            right_idx = (cur+1) * 2

            if right_idx < self.length:
                if self.max_heap[left_idx] < self.max_heap[right_idx]:
                    max_idx = right_idx
                else:
                    max_idx = left_idx
            elif left_idx < self.length:
                max_idx = left_idx
            else:
                break
            
            if self.max_heap[cur] < self.max_heap[max_idx]:
                self.max_heap[cur], self.max_heap[max_idx] = self.max_heap[max_idx], self.max_heap[cur]
                cur = max_idx
            else:
                break
        self.min_heap.remove(max_val)
        return max_val

    def pop_min(self):
        # 비어 있는 경우
        if self.length == 0:
            return 0
        # 비어 있지 않은 경우
        self.length -= 1
        if self.length == 0:
            self.max_heap.pop()
            return self.min_heap.pop()

        # for min heap
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        min_val = self.min_heap.pop()
        cur = 0
        while True:
            left_idx = (cur+1) * 2 - 1
            right_idx = (cur+1) * 2

            if right_idx < self.length:
                if self.min_heap[left_idx] > self.min_heap[right_idx]:
                    min_idx = right_idx
                else:
                    min_idx = left_idx
            elif left_idx < self.length:
                min_idx = left_idx
            else:
                break
            
            if self.min_heap[cur] > self.min_heap[min_idx]:
                self.min_heap[cur], self.min_heap[min_idx] = self.min_heap[min_idx], self.min_heap[cur]
                cur = min_idx
            else:
                break
        self.max_heap.remove(min_val)
        return min_val



def solution(operations):
    heap = Heap()
    for ops in operations:
        op, val = ops.split(' ')
        if op == 'I':
            heap.push(int(val))
        if op == 'D':
            if val == '1':
                val = heap.pop_max()
            elif val == '-1':
                val = heap.pop_min()

    return [heap.pop_max(), heap.pop_min()]

operations = ["I 16","D 1"]
result = [0, 0]
if solution(operations) == result:
    print('Success')
else:
    print('Fail')

operations = ["I 7","I 5","I -5","D -1"]	
result = [7, 5]
if solution(operations) == result:
    print('Success')
else:
    print('Fail')

# heapq 사용한 풀이
import heapq
def solution(operations):
    answer = []
    length = 0
    for ops in operations:
        op, val = ops.split(' ')
        if op == 'I':
            heapq.heappush(answer, int(val))
            length += 1
        if op == 'D':
            if length == 0:
                continue
            length -= 1
            if val == '1':
                heapq._heapify_max(answer)
                heapq._heappop_max(answer)
                heapq.heapify(answer)
            elif val == '-1':
                heapq.heappop(answer)

    if length == 0:
        answer = [0, 0]
    elif length == 1:
        answer = [answer[0], answer[0]]
    else:
        min_val = heapq.heappop(answer)
        heapq._heapify_max(answer)
        max_val = heapq._heappop_max(answer)
        answer = [max_val, min_val]
    return answer

operations = ["I 16","D 1"]
result = [0, 0]
if solution(operations) == result:
    print('Success')
else:
    print('Fail')

operations = ["I 7","I 5","I -5","D -1"]	
result = [7, 5]
if solution(operations) == result:
    print('Success')
else:
    print('Fail')