'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}  # create two dictionaries to store character frequencies

        if len(s) != len(t):
            return False  # if lengths differ, they cannot be anagrams

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # count occurrences of each character in s
            countT[t[i]] = 1 + countT.get(t[i], 0)  # count occurrences of each character in t

        for c in countS:
            if countS[c] != countT.get(c, 0):  # compare frequency of same character in both strings
                return False  # if any mismatch, not an anagram

        return True  # all character counts match, so it is an anagram
'''
Walkthrough Example
Input:
s = "anagram"
t = "nagaram"
Step 1: Length check
len(s) = 7
len(t) = 7 → continue
Step 2: Build frequency maps

After loop:

countS:
a:3
n:1
g:1
r:1
m:1
countT:
n:1
a:3
g:1
r:1
m:1
Step 3: Compare counts

Loop through countS:

c = 'a' → 3 == 3 
c = 'n' → 1 == 1 
c = 'g' → 1 == 1 
c = 'r' → 1 == 1 
c = 'm' → 1 == 1 
Final:
True
Quick failure example
s = "rat"
t = "car"
countS:
r:1, a:1, t:1
countT:
c:1, a:1, r:1

Check:

t → countS = 1, countT = 0 

 return False

Complexity
Time Complexity: O(n)
Space Complexity: O(1)  (since alphabet size is fixed, e.g., 26 letters)
'''