'''

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
'''
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Track the length of the longest sequence found
        longest = 0
        # Convert list to set for O(1) membership checks
        set_nums = set(nums)

        # Iterate each unique number; start building a sequence only if
        # the current number is the beginning of a sequence (num-1 not present)
        for num in set_nums:
            if num - 1 not in set_nums:
                current = num  # start value of this consecutive sequence
                length = 1  # current sequence length
                # extend the sequence while the next number exists in the set
                while current + 1 in set_nums:
                    length += 1
                    current += 1
                # update longest if this sequence is longer
                longest = max(longest, length)

        return longest

# Walkthrough Example:
# nums = [100,4,200,1,3,2]
# Convert to set -> {1,2,3,4,100,200}
# Start with 1 (since 0 not in set): extend to 2,3,4 -> length 4
# Other starts either have predecessors or produce shorter lengths -> answer 4

# Time Complexity: O(n) on average — each number is visited a constant number of times.
# Space Complexity: O(n) for the set used to get O(1) lookups.