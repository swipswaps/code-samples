""" buildPalindrome
Given a string, find the shortest possible string which can be achieved by adding characters 
to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string st

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    3 ≤ st.length ≤ 10.

    [output] string
"""


def buildPalindrome(st):
    i = 0
    while st[i:] != st[i:][::-1]:
        i += 1
    return st if i == 0 else st + st[i-1::-1]    


print(buildPalindrome("abcdc")) # "abcdcba"
