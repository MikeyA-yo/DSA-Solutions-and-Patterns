'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 
'''

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # define 32-bit integer limits

        sign = -1 if x < 0 else 1  # store whether the number is negative or positive
        x_abs = abs(x)  # convert number to positive for easier reversal

        reversed_str = str(x_abs)[::-1]  # convert number to string and reverse it
        reversed_int = sign * int(reversed_str)  # convert back to integer and restore original sign

        if reversed_int < INT_MIN or reversed_int > INT_MAX:  # check if result is within 32-bit range
            return 0  # return 0 if it overflows

        return reversed_int  # return the valid reversed integer

'''
Walkthrough Example
Input:
x = -123
Step 1: Define limits
INT_MIN = -2147483648
INT_MAX = 2147483647
Step 2: Determine sign
x = -123 → sign = -1
Step 3: Convert to absolute value
x_abs = 123
Step 4: Reverse digits as string
str(123) → "123"
"123"[::-1] → "321"
Step 5: Convert back to integer and apply sign
reversed_int = -1 * 321 = -321
Step 6: Check overflow
-321 is within range → valid
Final Output:
-321
Another Example (overflow case)
Input:
x = 1534236469
Reverse:
9646324351
Check:
9646324351 > INT_MAX → overflow
Output:
0
Time and Space Complexity
Time Complexity: O(n)      # where n is number of digits
Space Complexity: O(n)    # due to string conversion
'''