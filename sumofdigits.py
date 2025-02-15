num = int(input("enter your value"))

sum = 0
i = 0

while num > 0:
    i = num % 10
    sum = sum + i
    num = num // 10

print("The sum of the didgits of your number is", sum)
