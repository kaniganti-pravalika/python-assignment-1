'''560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
 
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2


Example 2:
Input: nums = [1,2,3], k = 3
Output: 2'''


class Solution:
    def subarraySum(self, nums):
        total_subarray = 0
        for i in range(len(nums)):
            sum=0
            for j in range(i, len(nums)):
                sum+=nums[j]
                if sum==k:
                    total_subarray+=1
        return total_subarray






'''303. Range Sum Query - Immutable
Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 
Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]


Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3'''


class NumArray:


    def __init__(self, nums):
        self.nums = nums
       


    def sumRange(self, left: int, right: int) -> int:
        t = 0
        for i in range(left,(right+1)):
            t += self.nums[i]
        return t



'''520. Detect Capital


We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
 
Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false
'''

class Solution:
    def detectCapitalUse(self, word):
        if len(word)==1: return True
        return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())






 #mini project on File handling
import os

FILE_NAME = "notes.txt"

def write_note():
    content = input("Write your note:\n")
    with open(FILE_NAME, "w") as file:
        file.write(content)
    print("Note saved successfully!\n")


def append_note():
    content = input("Write additional content:\n")
    with open(FILE_NAME, "a") as file:
        file.write("\n" + content)
    print("Content added successfully!\n")


def read_note():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            print("\n--- Your Notes ---")
            print(file.read())
            print()
    else:
        print("No notes found!\n")


def delete_notes():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("Notes file deleted successfully!\n")
    else:
        print("No notes file exists!\n")


while True:
    print("===== Notes Saver System =====")
    print("1. Write New Note")
    print("2. Add to Existing Note")
    print("3. Read Notes")
    print("4. Delete Notes File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_note()
    elif choice == "2":
        append_note()
    elif choice == "3":
        read_note()
    elif choice == "4":
        delete_notes()
    elif choice == "5":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice!\n")

'''Output
===== Notes Saver System =====
1. Write New Note
2. Add to Existing Note
3. Read Notes
4. Delete Notes File
5. Exit
Enter your choice: 1

Write your note:
Today I learned about file handling in Python.
Note saved successfully!


===== Notes Saver System =====
1. Write New Note
2. Add to Existing Note
3. Read Notes
4. Delete Notes File
5. Exit
Enter your choice: 2

Write additional content:
It is used to store data permanently.
Content added successfully!


===== Notes Saver System =====
1. Write New Note
2. Add to Existing Note
3. Read Notes
4. Delete Notes File
5. Exit
Enter your choice: 3

--- Your Notes ---
Today I learned about file handling in Python.
It is used to store data permanently.


===== Notes Saver System =====
1. Write New Note
2. Add to Existing Note
3. Read Notes
4. Delete Notes File
5. Exit
Enter your choice: 4

Notes file deleted successfully!


===== Notes Saver System =====
1. Write New Note
2. Add to Existing Note
3. Read Notes
4. Delete Notes File
5. Exit
Enter your choice: 5

Exiting Program...'''

