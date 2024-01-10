/*
Given a string s, return the longest
palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

*/
public class longestPalindrome {
    public static String longestPalindrome(String s) {

        String temp[] = new String[s.length()];
        ArrayList answer = new ArrayList();
        ArrayList end = new ArrayList();
        if(s.length()==1){
            end.add(s);
        }
        for (int i = 0; i < s.length(); i++) {
            temp[i] = s.substring(i, i + 1);
        }

        for (int j = 0; j < s.length() - 1; j++) {
            if (temp[j].equals(temp[j + 1])) {
                answer.add(temp[j]);
                answer.add(temp[j + 1]);
                for (int x = j - 1, y = j + 2; x >= 0 && y <= s.length() - 1; x--, y++) {
                    if (temp[x].equals(temp[y])) {
                        answer.add(0, temp[x]);
                        answer.add(temp[y]);
                    } else {
                        break;
                    }
                }

                end.add(String.join("",answer));
                answer.clear();
            }

            answer.add(temp[j]);
            for (int x = j - 1, y = j + 1; x >= 0 && y <= s.length() - 1; x--, y++) {
                if (temp[x].equals(temp[y])) {
                    answer.add(0, temp[x]);
                    answer.add(temp[y]);
                } else {
                    break;
                }
            }
            end.add(String.join("",answer));
            answer.clear();


        }
        int liczba = 0;
        int max = 0;
        for(int i=0;i<end.size();i++){
            int current = end.get(i).toString().length();
            if (current > max) {
                max = current;
                liczba = i;
            }
        }
        return end.get(liczba).toString();
    }
}