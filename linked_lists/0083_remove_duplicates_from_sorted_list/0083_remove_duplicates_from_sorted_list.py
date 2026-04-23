"""83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.

Example: 1 -> 1 -> 2 -> 3 -> 3  =>  1 -> 2 -> 3

Strategy: single pass with a trailing pointer
Because the list is sorted, duplicates are always adjacent.
Bypass duplicate next nodes without advancing; only advance on a value change.
"""

from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    if not head:
        return None

    current = head

    while current.next:
        if current.val == current.next.val:
            # Duplicate found: unlink the next node.
            current.next = current.next.next
        else:
            # Different value: safe to move forward.
            current = current.next

    return head


"""
Walkthrough — 1 -> 1 -> 2 -> 3 -> 3

current=1: val(1)==next.val(1) -> unlink  =>  1 -> 2 -> 3 -> 3
current=1: val(1)!=next.val(2) -> advance
current=2: val(2)!=next.val(3) -> advance
current=3: val(3)==next.val(3) -> unlink  =>  1 -> 2 -> 3
current=3: next is None -> loop ends

Return: 1 -> 2 -> 3

Why we stay in place after unlinking:
  The new current.next hasn't been checked yet and could be another
  duplicate. Staying catches runs like 1 -> 1 -> 1 -> 2 correctly.

Time Complexity:  O(n) — each node is visited at most once
Space Complexity: O(1) — pointers only, no extra data structures
"""
