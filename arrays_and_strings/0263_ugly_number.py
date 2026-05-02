'''
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.
Example 3:

Input: n = 14
Output: false
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers are positive by definition; non-positive numbers are not ugly
        if n <= 0:
            return False

        # remove all factors of 2, 3, and 5
        for factor in [2, 3, 5]:
            # keep dividing n by the factor while divisible
            while n % factor == 0:
                n = n // factor

        # if after removing all 2,3,5 factors we are left with 1,
        # then n had no other prime factors and is ugly
        return n == 1

# Walkthrough Example:
# n = 6 -> divide by 2 => 3, divide by 3 => 1 -> returns True
# n = 14 -> divide by 2 => 7, 7 not divisible by 3 or 5 -> returns False

# Time Complexity: O(log n) in number of divisions (each division reduces n), worst-case O(log n).
# Space Complexity: O(1) — constant extra space.