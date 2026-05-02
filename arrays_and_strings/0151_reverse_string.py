'''
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.'''
class Solution(object):
    def reverseWords(self, s):
        # split() with no arguments splits on any whitespace and removes extras
        splitted = s.split()
        # reverse the list of words in place
        splitted.reverse()
        # join with a single space to form the result string
        return " ".join(splitted)

# Walkthrough Example:
# s = "  hello   world  " -> s.split() => ["hello","world"] -> reversed -> ["world","hello"]
# join -> "world hello"

# Time Complexity: O(n) where n is the length of s (splitting and joining traverse the string).
# Space Complexity: O(n) for the list of words and the result string.
        