'''prime or not
num = int(input("Enter number: "))
if num <= 1:
    print("Not Prime Number")
else:
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        print("Prime Number")
    else:
        print("Not Prime Number")
num = int(input("Enter number: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
if reverse == num:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")
num = int(input("Enter number: "))
total = 0
for i in range(1, num):
        if num % i == 0:
            total = total + i
if total == num:
        print("Perfect Number")
else:
        print("Not Perfect Number")

num = int(input("Enter number: "))
    
while num > 9:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit
            num //= 10
        num = total
        
if num == 1:
        print("Magic Number")
else:
        print("Not Magic Number")'''
num = int(input("Enter number: "))
    
if num <= 0:
    print("Not Ugly Number")
else:
    for i in [2, 3, 5]:
        while num % i == 0:
                num //= i
        
    if num == 1:
            print("Ugly Number")
    else:
            print("Not Ugly Number")