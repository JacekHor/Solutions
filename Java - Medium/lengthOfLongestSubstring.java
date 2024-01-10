/*
Given a string s, find the length of the longest
substringwithout repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */
import java.util.ArrayList;

public class lengthOfLongestSubstring {
    public static int lengthOfLongestSubstring(String s) {
        String temp[] = new String[s.length()];
        ArrayList word = new ArrayList();
        int answer = 0;
        for(int i = 0; i<s.length(); i++){
            temp[i] = s.substring(i,i+1);
        }

        for(int i = 0; i<s.length(); i++) {
            word.add(temp[i]);
            if(word.size()>answer){
                answer = word.size();
            }
            for (int j = i + 1; j < s.length(); j++) {
                if (word.contains(temp[j])) {
                    if(word.size()>answer){
                        answer = word.size();
                    }
                    word.clear();
                    break;
                } else {
                    word.add(temp[j]);
                    if(word.size()>answer){
                        answer = word.size();
                    }
                }
            }
            word.clear();
        }
        return answer;
    }
}