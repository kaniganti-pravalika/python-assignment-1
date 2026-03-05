'''1.A popular e-commerce website stores millions of user passwords. For security reasons, the website never displays the full password on the screen. Instead, when showing password hints or logs, all characters of the password are hidden using *, except the last two characters, which are kept visible to help users recognize their password.
Input Format
A single string S representing the password
Constraints
NA
Output Format
Print the masked password where the last two characters remain unchanged and all other characters are replaced with *
Sample Input 0
hello123


Sample Output 0
******23


Sample Input 1
A1B2C3D4


Sample Output 1
******D4


Sample Input 2
ab


Sample Output 2
ab


Contest ends in 18 hours
Submissions: 13
Max Score: 50
Difficulty: Medium
Rate This Challenge:
    
More
 
1'''
s = input().strip()
if len(s) <= 2:

   print(s)

else:

   masked = "*" * (len(s) - 2) + s[-2:]

   print(masked)


'''2.An oil factory has N number of containers and each has a different capacity. During renovation, the manager decided to make some changes with the containers. He wishes to make different pairs for the containers in such a way that in the first pair, the container of maximum capacity is paired with the container of minimum capacity, and so on for the rest of the containers, to maintain a balance throughout all the pairs of containers. Write an algorithm to make different pairs of containers in such a way that the first container in the pair is of maximum capacity and second container in the pair is of minimum capacity.
Input Format
The first line of the input consists of an integer - numContainers, representing the number of containers (N). The next line consists of N space-separated integers - cont1, cont2, .... contN, representing container capacity.
Constraints
NA
Output Format
Print K lines consisting of two space-separated integers representing the pairs that will be formed to maintain the balance by pairing the container of maximum capacity with the container of minimum capacity and so on. Note If only one container is left and no pair is possible then print the capacity of that container and the second value will be '0'.
Sample Input 0
6
100 560 23 19 53 20


Sample Output 0
560 19
100 20
53 23


Sample Input 1
5
15 25 35 45 55


Sample Output 1
55 15
45 25
35 0


Sample Input 2
2
3 7


Sample Output 2
7 3
Code:'''

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = n - 1

while left < right:
    print(arr[right], arr[left])
    left += 1
    right -= 1

if left == right:
    print(arr[right], 0)
'''3.Alice and Bob are given two strings. Alice claims that one string is a permutation of the other if both strings contain the same characters with the same frequency, but possibly in a different order. Bob is not convinced and asks you to verify this.
Write a program to determine whether one string is a permutation of the other.
Return True if the strings are permutations of each other, otherwise return False.
Input Format
The first line contains a string S1. The second line contains a string S2.
Constraints
1≤𝑛≤10 Strings contain only lowercase English alphabets.
Output Format
Print True if one string is a permutation of the other, otherwise print False.
Sample Input 0
abc
cab


Sample Output 0
True


Sample Input 1
hello
olleh


Sample Output 1
True


Sample Input 2
aabbcc
abcabc


Sample Output 2
True'''




s1 = input().strip()
s2 = input().strip()

if sorted(s1) == sorted(s2):
    print("True")
else:
    print("False")

