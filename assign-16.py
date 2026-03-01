'''Two Pointer Approach
 Company  Amazon
 Problem:
Find two package weights (sorted array) whose sum equals target.
Code:'''

def find_package_pair(weights, target):
   left = 0
   right = len(weights) - 1

   while left < right:
       current_sum = weights[left] + weights[right]

       if current_sum == target:
           return [left + 1, right + 1]   # 1-based index
       elif current_sum < target:
           left += 1
       else:
           right -= 1

   return [-1, -1]


# Example
weights = [2, 4, 7, 11, 15]
target = 15
print(find_package_pair(weights, target))
'''Output:
[2, 3]'''

'''Prefix-Suffix Sum
 Company : Microsoft
Problem
Find index where sum of elements before equals sum after.
Code'''
def find_stability_day(loads):
   total_sum = sum(loads)
   prefix_sum = 0

   for i in range(len(loads)):
       if prefix_sum == total_sum - prefix_sum - loads[i]:
           return i
       prefix_sum += loads[i]

   return -1


# Example
loads = [3, 4, 8, -9, 20, 6]
print(find_stability_day(loads))


'''Output:
loads = [3, 4, 8, -9, 20, 6]'''

4
''' Sliding Window
 Company  Google
 Problem: Find maximum sum of any subarray of size k.
Code:'''

def max_active_users(users, k):
   n = len(users)
  
   # Initial window sum
   window_sum = sum(users[:k])
   max_sum = window_sum

   for i in range(k, n):
       window_sum = window_sum - users[i - k] + users[i]
       max_sum = max(max_sum, window_sum)

   return max_sum


# Example
users = [100, 200, 300, 400, 250, 100, 500]
k = 3
print(max_active_users(users, k))

'''Output:
users = [100, 200, 300, 400, 250, 100, 500]
k = 3
950

'''