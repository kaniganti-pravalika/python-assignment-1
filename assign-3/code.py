'''9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
 '''
class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

''''66. Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
 '''
class Solution(object):
    def plusOne(self, digits):
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits
     

'''258. Add Digits
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
 '''

class Solution(object):
    def addDigits(self, num):
        while num>=10:
            total=0
            while num>0:
                total+=num%10
                num//=10
            num=total
        return num
        

''' Convert a Number to Hexadecimal
Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem.
 '''
class Solution:
    def digitToHexChar(self, digit):
        # Convert a single digit (0-15) to its hexadecimal character
        hex_chars = "0123456789abcdef"
        return hex_chars[digit]


    def toHex(self, num):
       
        if num == 0:
            return "0"
       
       
        if num < 0:
            num += 2 ** 32
       
        hex_str = ""
        while num > 0:
            digit = num % 16
            hex_str = self.digitToHexChar(digit) + hex_str
            num //= 16
       
        return hex_str



''' Count the Digits That Divide a Number
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.'''
class Solution:
    def countDigits(self, num):
        count = 0
        for digit_char in str(num):
            digit = int(digit_char)
            if digit != 0 and num % digit == 0:
                count += 1
        return count



