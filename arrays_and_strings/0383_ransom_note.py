'''
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}  
        # dictionary to store how many times each letter appears in magazine

        for letter in magazine:
            count[letter] = count.get(letter, 0) + 1  
            # count frequency of each character in magazine
            # if letter not seen before → start from 0, then add 1

        for letter in ransomNote:
            if letter not in count or count[letter] == 0:
                # if letter doesn't exist OR we have used all available copies
                return False

            count[letter] -= 1  
            # use one occurrence of this letter (consume it)

        return True  
        # if we successfully matched all letters in ransomNote, return True
'''
 Walkthrough Example
Input:
ransomNote = "aa"magazine = "aab"

Step 1: Build frequency map from magazine
count = {    'a': 2,    'b': 1}

Step 2: Process ransomNote

letter = 'a'
count['a'] = 2 → use 1 → becomes 1

letter = 'a'
count['a'] = 1 → use 1 → becomes 0

Step 3: Done
All letters successfully matched.
return True

 Failure Example
Input:
ransomNote = "aa"magazine = "ab"

Step 1:
count = {'a':1, 'b':1}

Step 2:


first 'a' → OK → becomes 0


second 'a' → not enough → 0 →  return False

 Complexity
Time Complexity: O(n + m)- n = length of magazine- m = length of ransomNoteSpace Complexity: O(1)- at most 26 letters (constant alphabet size)

 Final Takeaway

You build a supply (magazine), then try to consume it (ransomNote). If anything runs out, return False.


If you want next, I can show you:


how this connects to "Find the Difference" problem (same pattern)


or how to instantly recognize when to use this frequency-consumption pattern in interviews


'''