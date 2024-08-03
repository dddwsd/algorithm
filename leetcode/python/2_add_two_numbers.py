# https://leetcode.com/problems/add-two-numbers/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        point = 0
        answer = 0
        while l1 or l2:
            print(l1.val, l2.val)
            if l1:
                answer += l1.val * (10 ** point)
                l1 = l1.next
            if l2:
                answer += l2.val * (10 ** point)
                l2 = l2.next
            print(answer, point, l1, l2)
            point += 1
        
        answer = list(str(answer))[::-1]
        val = answer.pop(0)
        head = cur = ListNode(int(val))
        for val in answer:
            cur.next = ListNode(int(val))
            cur = cur.next
        return head

solution = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

output = ListNode(7)
output.next = ListNode(0)
output.next.next = ListNode(8)

result = solution.addTwoNumbers(l1, l2)

def check(output, result):
    while output:
        print(output.val, result.val)
        if output.val == result.val:
            output = output.next
            result = result.next
        else:
            return False
    return True
if check(output, result):
    print('Success')
else:
    print('Fail')