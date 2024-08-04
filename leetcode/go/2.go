/*
2 - Add Two Numbers
*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime
13ms / 15.89%
Memory
4.51MB / 23.78%
*/
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	node := &ListNode{}
	head := node
	sum := 0
	carry := 0

	for l1 != nil || l2 != nil {
		sum = 0
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}

		sum += carry
		carry = sum / 10
		sum %= 10
		node.Next = &ListNode{Val: sum}
		node = node.Next
	}

	if carry != 0 {
		node.Next = &ListNode{Val: carry}
	}

	return head.Next
}
