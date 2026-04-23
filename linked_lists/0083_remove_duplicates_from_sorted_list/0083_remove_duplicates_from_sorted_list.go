// 83. Remove Duplicates from Sorted List
//
// Given the head of a sorted linked list, delete all duplicates such that
// each element appears only once. Return the linked list sorted as well.
//
// Example: 1 -> 1 -> 2 -> 3 -> 3  =>  1 -> 2 -> 3

// Strategy: single pass with a trailing pointer
// Because the list is sorted, duplicates are always adjacent.
// Bypass duplicate next nodes without advancing; only advance on a value change.

package linkedlists

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	current := head

	for current.Next != nil {
		if current.Val == current.Next.Val {
			// Duplicate found: unlink the next node.
			current.Next = current.Next.Next
		} else {
			// Different value: safe to move forward.
			current = current.Next
		}
	}

	return head
}

/*
Walkthrough — 1 -> 1 -> 2 -> 3 -> 3

current=1: Val(1)==Next.Val(1) -> unlink  =>  1 -> 2 -> 3 -> 3
current=1: Val(1)!=Next.Val(2) -> advance
current=2: Val(2)!=Next.Val(3) -> advance
current=3: Val(3)==Next.Val(3) -> unlink  =>  1 -> 2 -> 3
current=3: Next==nil -> loop ends

Return: 1 -> 2 -> 3

Time Complexity:  O(n) — each node is visited at most once
Space Complexity: O(1) — pointers only, no extra data structures
*/
