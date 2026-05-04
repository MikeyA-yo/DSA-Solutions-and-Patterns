'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        # count frequency of each character
        count = Counter(s)
        length = 0
        odd_found = False

        # for every character, if its count is even we can use all of them
        # if it's odd, we can use count-1 (an even number) and potentially
        # place one odd character in the center of the palindrome
        for char in count:
            if count[char] % 2 == 0:
                length += count[char]
            else:
                length += count[char] - 1
                odd_found = True

        # if any odd-count character existed, we can put one in the center
        if odd_found:
            length += 1

        return length

# Walkthrough Example:
# s = "abccccdd" -> counts: {c:4,d:2,a:1,b:1}
# use all of c (4) and d (2) = 6, a and b contribute 0 each but one odd can be center -> +1 => 7

# Time Complexity: O(n) to build counts and iterate characters.
# Space Complexity: O(k) where k is number of distinct characters (up to O(n)).
        