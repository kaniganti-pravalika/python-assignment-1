num1 = int(input())
num2 = int(input())

l = []

if num1 < num2:
    for i in range(num1, num2):
        if i < 50 and i % 5 == 0 and 10 <= i <= 99:
            digit_sum = (i // 10) + (i % 10)
            if digit_sum % 3 == 0:
                l.append(i)

print(l)

if l:
    print(max(l))
else:
    print("No valid numbers found")