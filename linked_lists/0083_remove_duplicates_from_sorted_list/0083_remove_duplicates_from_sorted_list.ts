// 83. Remove Duplicates from Sorted List
//
// Given the head of a sorted linked list, delete all duplicates such that
// each element appears only once. Return the linked list sorted as well.
//
// Example: 1 -> 1 -> 2 -> 3 -> 3  =>  1 -> 2 -> 3

// Definition for singly-linked list.
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

// Strategy: single pass with a trailing pointer
// Because the list is already sorted, duplicates are always adjacent.
// Walk current forward; whenever the next node has the same value, bypass it
// by pointing current.next to current.next.next (skipping the duplicate).
// Only advance current when the next node is a different value.

function deleteDuplicates(head: ListNode | null): ListNode | null {
    if (!head) return null;

    let current = head;

    while (current.next) {
        if (current.val === current.next.val) {
            // Duplicate found: unlink the next node.
            current.next = current.next.next;
        } else {
            // Different value: safe to move forward.
            current = current.next;
        }
    }

    return head;
}

/*
Walkthrough — 1 -> 1 -> 2 -> 3 -> 3

current=1: current.val(1) == current.next.val(1) -> unlink
  list: 1 -> 2 -> 3 -> 3
current=1: current.val(1) != current.next.val(2) -> advance
current=2: current.val(2) != current.next.val(3) -> advance
current=3: current.val(3) == current.next.val(3) -> unlink
  list: 1 -> 2 -> 3
current=3: current.next is null -> loop ends

Return: 1 -> 2 -> 3

Why we don't advance after unlinking:
  After bypassing a duplicate, current.next is now a new node we haven't
  checked yet — it could itself be another duplicate of current.val.
  Staying in place ensures we catch runs of 3 or more identical values.

Example — 1 -> 1 -> 1 -> 2:
  current=1: unlink -> 1 -> 1 -> 2  (stay)
  current=1: unlink -> 1 -> 2       (stay)
  current=1: advance -> current=2
  current=2: next is null -> done    =>  1 -> 2  ✓

Time Complexity:  O(n) — each node is visited at most once
Space Complexity: O(1) — pointers only, no extra data structures
*/

export { deleteDuplicates, ListNode };
