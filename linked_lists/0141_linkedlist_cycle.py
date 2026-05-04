'''

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

class Solution:
    def hasCycle(self, head):
        # Use Floyd's Tortoise and Hare algorithm
        # slow moves one step, fast moves two steps
        slow = head
        fast = head

        # If there is a cycle, slow and fast will eventually meet inside the cycle
        while fast and fast.next:
            slow = slow.next         # move slow by one
            fast = fast.next.next    # move fast by two
            if slow == fast:
                return True

        # fast reached the end (None) -> no cycle
        return False

# Walkthrough Example:
# head = [3,2,0,-4] with tail connecting to node at pos=1
# slow and fast start at head; after some steps they meet inside the loop -> True

# Time Complexity: O(n) — both pointers move through the list at most a constant factor of n steps.
# Space Complexity: O(1) — constant extra space.
