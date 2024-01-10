'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        words = []
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs)):
            words.append(strs[i])

        wynik = ""

        for i in range(len(words[0])):
            temp = []
            for j in range(len(strs)):
                try:
                    temp.append(words[j][i])
                except:
                    return wynik
            temp2 = set(temp)
            if len(temp2) == 1:
                wynik += words[j][i]
            elif len(temp2) > 1:
                return wynik
            temp2 = set()
            temp = []
        return wynik