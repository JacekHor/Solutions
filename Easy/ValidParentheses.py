'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''
class Solution(object):
    def isValid(self, s):
        dic = {")": "(", "]": "[", "}": "{"}
        open = ("(", "[", "{")
        close = (")", "]", "}")

        wynik = []

        temp = len(s)
        if temp % 2 != 0:
            return False

        for i in range(temp):
            if s[i] in close and wynik == []:
                return False
            elif s[i] in open:
                wynik.append(s[i])
            elif s[i] in close and dic.get(s[i]) == wynik[len(wynik) - 1]:
                wynik.pop(len(wynik) - 1)
            else:
                return False
        if wynik == []:
            return True
        else:
            return False