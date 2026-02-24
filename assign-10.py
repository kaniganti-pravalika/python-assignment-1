#13 – Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        result=0
        roman_to_int={
            "I":1,
            "III":3,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }
        for i in range(len(s)):
            if i+1<len(s) and roman_to_int[s[i]]<roman_to_int[s[i+1]]:
                result-=roman_to_int[s[i]]
            else:
                result+=roman_to_int[s[i]]
        return result



'''
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.'''


 








#58 – Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                if count>0:
                    break
            else:
                count+=1
        return count
    
'''Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.'''

#28 – Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0  # edge case: empty needle


        for ch in range(len(haystack) - len(needle) + 1):
            if haystack[ch:ch+len(needle)] == needle:
                return ch
           
        return -1
'''Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.'''

