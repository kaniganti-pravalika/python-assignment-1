'''
You are given an array nums of positive integers and an integer k.

In one operation, you can remove the last element of the array and add it to your collection.

Return the minimum number of operations needed to collect elements 1, 2, ..., k.

'''
class Solution:
    def minOperations(self, nums,k):
        count=0
        l=set()
        for i in range(len(nums)-1,-1,-1):
            count+=1
            if nums[i]<=k:
                l.add(nums[i])
            if len(l)==k:
                return count
        return count
