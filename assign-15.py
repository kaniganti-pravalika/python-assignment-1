#sum of sub array
def max_sum_subarray(arr,k):
    n=len(arr)
    max_sum=0
    for i in range(n-k+1):#6-3+1-->[4]-->0123
        current_sum=0
        for j in range(i,i+k):#0,0+3-->(0,3)-->0,1,2
            current_sum+=arr[j]
        max_sum=max(max_sum,current_sum)
    return max_sum
print(max_sum_subarray([2,1,5,1,3,7],3))

#sliding window
def max_sum_subarry(arr,k):
    window_sum=sum(arr[:k])#012
    max_sum=window_sum
    for i in range(k,len(arr)):#3,6-->3,4,5
        window_sum+arr[i]-arr[i-k]
        max_sum=max(max_sum,window_sum)#1-2-->-1+8-->7
    return max_sum
print(max_sum_subarray([2,1,5,1,3,7],3))

#longest_unique_substring using brute force approach
def longest_unique_substring(s):
    n=len(s)#8
    max_len=0
    for i in range(n):
        for j in range(i,n):
            substring=s[i:j+1]
            if len(set(substring))==len(substring):
                max_len=max(max_len,j-i+1)
    return max_len
print(longest_unique_substring("abcabcbb"))
#using sliding window
def longest_unique_substring(s):
    left=0
    seen=set()
    max_len=0
    for right in range (len(s)):
        while s[right]in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_len=max(max_len,right-left+1)
    return max_len
print(longest_unique_substring("abcabcbb"))